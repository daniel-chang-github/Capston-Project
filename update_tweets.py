import get_twitter_data
import db_functions
import data_load_twitter

#Get the list of usernames to download from the twitter_user table.
download_list = db_functions.get_twitter_user()

#Loop through the twitter user ids and download and import tweets.
for i in range(len(download_list)):
    #Download tweets.
    get_twitter_data.get_tweets(download_list[i]['user_id'])

    #Upload tweets.
    data_load_twitter.import_twitter(download_list[i]['user_id'])
