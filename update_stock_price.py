import get_company_info
import db_functions
import data_load_stock_price

#Get the list of tickers to download from the ticker_list table.
download_list = db_functions.get_ticker_list()

#Loop through the twitter user ids and download and import tweets.
for i in range(len(download_list)):
    #Download stock price.
    get_company_info.dl_prices(download_list[i]['ticker'])

    #Upload stock price.
    data_load_stock_price.import_prices(download_list[i]['ticker'])
