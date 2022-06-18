import config
import tweepy
import pandas as pd
from pathlib import Path # To create necessary folders
from datetime import datetime
import log

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)

# Create API object
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

#default path for the data.
save_path = 'data/tweets/'

def get_tweets(user_id_input):

    try:
        tweets = api.user_timeline(screen_name=user_id_input, 
                            # 200 is the maximum allowed count
                            count=400,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )

        #Finding the tweet with only ticker symbol tagged.
        list = []
        for i in range(len(tweets)):
            # print((tweets[0]['created_at']))
            # print(i,(tweets[i]['entities']['symbols']))
            for element in (tweets[i]['entities']['symbols']):
                list.append({                 
                    'user_id' : user_id_input
                    ,'created_at' : tweets[i]['created_at']
                    ,'id' : tweets[i]['id']
                    ,'full_text' : tweets[i]['full_text']
                    ,'ticker' : element['text'] })

        output_file = 'tweets - {} - {}.csv'.format(user_id_input, datetime.now())
        output_dir = Path('data/tweets/{}'.format(user_id_input))
        output_dir.mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame.from_records(list)
        df.to_csv(save_path+user_id_input + '/' + user_id_input + output_file)
        log.logger.info('get_tweet - Success! - {} - {}'.format(user_id_input, datetime.now()))

    except:
        log.logger.warning('get_tweet - Download failed - Is the username correct? - {} - {}'.format(user_id_input, datetime.now()))



