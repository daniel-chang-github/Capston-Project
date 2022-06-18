import schedule
import time
import os


def update_tweets():
    os.system('python3 update_tweets.py')

def update_gov_official_trans():
    os.system('python3 update_gov_official_trans.py')

def update_stock_price():
    os.system('python3 update_stock_price.py')

schedule.every(10).minutes.do(update_tweets)
schedule.every().day.at('10:00').do(update_gov_official_trans())
schedule.every().day.at('22:00').do(update_stock_price())

while True:
 
    # Checks whether a scheduled task   
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)