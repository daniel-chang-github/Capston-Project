#%%
import pandas as pd
import os
from sqlalchemy import text
import glob
import os
from datetime import datetime 
import db_functions
import log

#%%
# Create a database connection
engine = db_functions.connect_db()

# default path for the data to be loaded
data_path = 'data/tweets'

#%%
# This function will build out the sql insert statement to insert new rows. Duplicated will be ignored.
def import_twitter(user_id):
    try:
        #Finding the lates file to try to upload
        list_of_files = glob.glob('{}/{}/*.csv'.format(data_path,user_id)) 
        latest_file = max(list_of_files, key=os.path.getctime)
        df = pd.read_csv(latest_file)
        
        # First part of the insert statement
        insert_init = """INSERT INTO tweets
                        (user_id, tweet_id, created_at, full_text, ticker)
                        VALUES
                    """

        # Second part of the insert statement
        vals = ",".join(["""('{}', '{}', '{}', '{}', '{}')""".format(
                        row.user_id,    
                        row.id,
                        row.created_at,
                        row.full_text.replace("'","''"),
                        row.ticker,

                        ) for index, row in df.iterrows()])

        # Skip the insert statement if it's duplicate value.
        insert_end = """ ON CONFLICT (tweet_id) DO NOTHING """

        # Put together the query string
        query = insert_init + vals + insert_end

        # Table row count before the upload.
        row_count_before = db_functions.get_table_row_count('tweets')

        # Fire insert statement
        engine.execute(text(query)) #text() takes care of the % in the query statement.

        # Table row count after the upload.
        row_count_after = db_functions.get_table_row_count('tweets')

        uploaded_rows = row_count_after - row_count_before
  
        log.logger.info('import_twitter - Upload successful - {} Uploaded rows - Import file used: {} - {}'.format(uploaded_rows, user_id, latest_file, datetime.now()))

    except:
        log.logger.warning('import_twitter - Upload FAILED - {} - Import file used: {} - {}'.format(user_id, latest_file, datetime.now()))



