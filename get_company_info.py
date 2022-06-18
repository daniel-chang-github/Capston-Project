from cmath import log
import csv
from tkinter import Y
import pandas as pd
import yfinance as yf    
from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_analysts_info, get_balance_sheet, get_cash_flow, get_cash_flow
# from yahoo_fin import news
import yahoo_fin as yahoo_f
from yahoo_fin import news ## How come this doesn't show up on yahoo_f?
import yahoo_fin.stock_info as si
from datetime import datetime
from pathlib import Path ## To create necessary folders
import log

#Only dl_prices() is being used at the moment.

def dl_prices(ticker_input):
    try:
        output_file = '{}_prices.csv'.format(ticker_input)
        output_dir = Path('data/prices/{}/{}'.format(ticker_input,datetime.now()))
        output_dir.mkdir(parents=True, exist_ok=True)

        yf_ticker = yf.Ticker(ticker_input)
        data = yf_ticker.history(period='MAX')
        data.to_csv(output_dir/output_file)
        log.logger.info('dl_prices - Download successful - {} - {}'.format(ticker_input, datetime.now()))
    except:
        log.logger.warning('dl_prices - Download FAILED - {} - {}'.format(ticker_input, datetime.now()))

def dl_financials(ticker_input):
    output_file = '{}_financials.csv'.format(ticker_input)
    output_dir = Path('data/financials/{}/{}'.format(ticker_input,datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    yf_ticker = yf.Ticker(ticker_input)
    data = yf_ticker.financials
    data.to_csv(output_dir/output_file)


def dl_major_holders(ticker_input):
    output_file = '{}_major_holders.csv'.format(ticker_input )
    output_dir = Path('data/holders/{}/{}'.format(ticker_input,datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    yf_ticker = yf.Ticker(ticker_input)
    data = yf_ticker.major_holders
    data.to_csv(output_dir/output_file)

def dl_institutional_holders(ticker_input):
    output_file = '{}_institutional_holders.csv'.format(ticker_input )
    output_dir = Path('data/holders/{}/{}'.format(ticker_input, datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    yf_ticker = yf.Ticker(ticker_input)
    data = yf_ticker.institutional_holders
    data.to_csv(output_dir/output_file)

def dl_recommendations(ticker_input):
    output_file = '{}_recommendations.csv'.format(ticker_input )
    output_dir = Path('data/recommendations/{}/{}'.format(ticker_input,datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    yf_ticker = yf.Ticker(ticker_input)
    data = yf_ticker.recommendations
    data.to_csv(output_dir/output_file)

def dl_analysts_info(ticker_input):    
    output_dir = Path('data/analysts_info/{}/{}'.format(ticker_input,datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    data = get_analysts_info(ticker_input)

    for k,v in data.items():  ##Dictionary to csv.
        # print((k))
        # print((v))
        v.to_csv(output_dir/'{} - {}.csv'.format(ticker_input, k))

def dl_balance_sheet(ticker_input):    
    output_file = '{}_balance_sheet.csv'.format(ticker_input)
    output_dir = Path('data/balance_sheet/{}/{}'.format(ticker_input, datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    data = get_balance_sheet(ticker_input)
    data.to_csv(output_dir/output_file)

def dl_cash_flow(ticker_input):    
    output_file = '{}_cash_flow.csv'.format(ticker_input)
    output_dir = Path('data/cash_flow/{}/{}'.format(ticker_input, datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    data = get_cash_flow(ticker_input)

    data.to_csv(output_dir/output_file)


def dl_news(ticker_input):  ##TODO: need to convert json to csv.
    output_file = '{}_news.csv'.format(ticker_input)
    output_dir = Path('data/news/{}/{}'.format(ticker_input,datetime.now()))
    output_dir.mkdir(parents=True, exist_ok=True)

    yf_ticker = yf.Ticker(ticker_input)
    data = pd.DataFrame(yf_ticker.news)

    data.to_csv(output_dir/output_file)






