
from sqlalchemy import create_engine, engine_from_config

def connect_db():
    db_password = ('1234')  # Set to your own password
    engine = create_engine('postgresql://postgres:{}@localhost/stock_db'.format(db_password))
    return engine


def get_table_row_count(talbe_name):
    query = """SELECT count(*) AS exact_count FROM {}""".format(talbe_name)
    result = connect_db().execute(query)
    return(result.fetchall()[0][0])


def add_ticker(ticker, name = None, sector = None):
    query = """INSERT INTO ticker_list 
                (ticker, name, sector)
                VALUES
                ('{}', '{}', '{}')
                ON CONFLICT (ticker) DO NOTHING 
                """.format(ticker, name, sector)
    engine = connect_db()
    engine.execute(query)

def add_tweeter_user (user_id):
    query = """INSERT INTO twitter_users 
                (user_id)
                VALUES
                ('{}')
                ON CONFLICT (user_id) DO NOTHING 
                """.format(user_id)
    engine = connect_db()
    engine.execute(query)


def get_ticker_list():
    engine = connect_db()
    query = ''' SELECT ticker FROM ticker_list
    '''
    result = engine.execute(query)
    return result.fetchall()

def get_twitter_user():
    engine = connect_db()
    query = ''' SELECT user_id FROM twitter_users
    '''
    result = engine.execute(query)
    return result.fetchall()


# add_tweeter_user()

# print(get_twitter_user())

# engine = connect_db()
# query = ''' SELECT user_id FROM twitter_users
# '''
# result = engine.execute(query)

# #Using fetchall() will give you a list of tuples (parentheses, single quotes, comma). Use scalar().
# print((result.fetchall()))


    