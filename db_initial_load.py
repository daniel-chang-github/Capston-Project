import db_functions
import pandas as pd

#%%
# Create a database connection
engine = db_functions.connect_db()


def load_ticker_list_from_csv(file = 'data/ticker/tracking_ticker_list.csv'):
    data = pd.read_csv(file)
    # First part of the insert statement
    insert_init =   """INSERT INTO ticker_list (ticker, name, sector) 
                    VALUES 
                    """

    # Add values for all days to the insert statement                
    vals = ",".join(["""('{}', '{}', '{}')""".format(
                    row.Symbol,
                    #to avoid errors when the name contains single quote. The single quote needs to be repalced to two single quotes.
                    row.Name.replace("'","''"), 
                    row.Sector
                    ) for index, row in data.iterrows()])

    # Handle duplicate values - Avoiding errors if you've already got some data in your table
    insert_end = """ ON CONFLICT (ticker) DO NOTHING """
    
    # Put together the query string
    query = insert_init + vals + insert_end

    engine.execute(query)

def load_ticker(ticker, name, sector):
    # First part of the insert statement
    insert_init =   """INSERT INTO ticker_list (ticker, name, sector) 
                    VALUES 
                    """

    # Add values for all days to the insert statement                
    vals = """('{}', '{}', '{}')""".format(ticker, name, sector)
                    

    # Handle duplicate values - Avoiding errors if you've already got some data in your table
    insert_end = """ ON CONFLICT (ticker) DO NOTHING """
    
    # Put together the query string
    query = insert_init + vals + insert_end

    engine.execute(query)



def load_twitter_user_id(user_id):

    # First part of the insert statement
    insert_init =   """INSERT INTO twitter_users (user_id) 
                    VALUES 
                    """

    # Add values for all days to the insert statement                
    vals = """('{}')""".format(user_id)

    # Handle duplicate values - Avoiding errors if you've already got some data in your table
    insert_end = """ ON CONFLICT (user_id) DO NOTHING """
    
    # Put together the query string
    query = insert_init + vals + insert_end

    engine.execute(query)

load_ticker('test2','test2','test2')



