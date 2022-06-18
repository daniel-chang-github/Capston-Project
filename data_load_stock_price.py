#%%
import pandas as pd
import os
import glob
import os
from datetime import datetime 
import db_functions
import log

#%%
# Create a database connection
engine = db_functions.connect_db()

# default path for the data to be loaded
prices_path = 'data/prices'
tickers_path = 'data/tickers'

#%%
# This function will build out the sql insert statement to insert new rows. Duplicated will be ignored.
def import_prices(ticker, path_input=prices_path):
    try:
        #Finding the lates file to try to upload
        list_of_files = glob.glob('{}/{}/*/*'.format(path_input,ticker)) 
        latest_file = max(list_of_files, key=os.path.getctime)
        df = pd.read_csv(latest_file, index_col=[0], parse_dates=[0])
        
        # Some clean up for missing data
        if 'dividend' not in df.columns:
            df['dividend'] = 0
        df = df.fillna(0.0)
        
        # First part of the insert statement
        insert_init = """INSERT INTO stock_price
                        (ticker, date, open, high,low ,close, volume, dividends, stock_splits, import_file_name)
                        VALUES
                    """

        # Second part of the insert statement
        vals = ",".join(["""('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}','{}')""".format(
                        ticker,    
                        index,
                        row['Open'],
                        row.High,
                        row.Low,
                        row.Close,
                        row.Volume,
                        row.Dividends,
                        row['Stock Splits'],
                        latest_file
                        ) for index, row in df[:4].iterrows()])

        # Skip the insert statement if it's duplicate value.
        insert_end = """ ON CONFLICT (ticker, date) DO NOTHING """

        # Put together the query string
        query = insert_init + vals + insert_end

        # Table row count before the upload.
        row_count_before = db_functions.get_table_row_count('stock_price')

        # Fire insert statement
        engine.execute(query)

        # Table row count after the upload.
        row_count_after = db_functions.get_table_row_count('stock_price')

        uploaded_rows = row_count_after - row_count_before
        
        log.logger.info('import_prices - Upload Successful - {} - {} Rows uploaded - Import file name: {} - {}'.format(ticker, uploaded_rows, latest_file, datetime.now()))
    except:
        log.logger.warning('import_prices - Upload FAILED - {} - Import file name: {}- {}'.format(ticker, latest_file, datetime.now()))

