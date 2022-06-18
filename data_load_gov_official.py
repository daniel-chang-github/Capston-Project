#%%
import pandas as pd
import os
from sqlalchemy import  text
import glob
import os
from datetime import datetime 
import db_functions
import log

#%%
# Create a database connection
engine = db_functions.connect_db()

# default path for the data to be loaded
data_path = 'data/gov_official'

#%%
# This function will build out the sql insert statement to insert new rows. Duplicated will be ignored.
def import_gov_official(data_path=data_path):
    try:
        #Finding the lates file to try to upload
        list_of_files = glob.glob('{}/*'.format(data_path)) 
        latest_file = max(list_of_files, key=os.path.getctime)
        df = pd.read_json(latest_file)
        df.fillna("0",inplace= True)
        # df.to_csv('export.csv')

        # First part of the insert statement
        insert_init = """INSERT INTO gov_official_trans
                        (disclosure_year, disclosure_date, transaction_date, owner, ticker, asset_description, type, amount, representative, link_to_report, cap_gains_over_200_usd, import_file_name)
                        VALUES
                    """

        # Second part of the insert statement
        vals = ",".join(["""('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}')""".format(
                        row.disclosure_year,    
                        row.disclosure_date.replace("'","''"),
                        row.transaction_date.replace("'","''"),
                        row.owner,
                        row.ticker.replace("'","''"),
                        row.asset_description.replace('"',"'").replace("'","''"),  #Replacing dobule quote to single quote as it single quote is necessary for strings with mixed cases. Also, replacing single quotes to dobule single quotes to the single quote doesn't interfere with query. 
                        row.type.replace("'","''"),
                        row.amount.replace("'","''"),
                        row.representative.replace("'","''"),
                        row.ptr_link.replace("'","''"),
                        row.cap_gains_over_200_usd,
                        latest_file
                        ) for index, row in df.iterrows()])
        
        # Skip the insert statement if it's duplicate value. 
        insert_end = """ ON CONFLICT (ticker, representative, disclosure_date, transaction_date, amount) DO NOTHING """

        # Put together the query string.
        query = insert_init + vals + insert_end

        # Table row count before the upload.
        row_count_before = db_functions.get_table_row_count('gov_official_trans')
        # Fire insert statement.
        engine.execute(text(query))  #Text() takes care of the issue with " % " in the query. 

        # Table row count after the upload.
        row_count_after = db_functions.get_table_row_count('gov_official_trans')

        uploaded_rows = row_count_after - row_count_before

        log.logger.info('import_gov_official - Upload successful - {} Rows uploaded - Import file name: {} - {} '.format(uploaded_rows, latest_file, datetime.now()))

    except: 
        log.logger.warning('import_gov_official - Upload FAILED - Import file name: {} - {}'.format(latest_file, datetime.now()))



