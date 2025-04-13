# mainapp/tasks.py
from celery import shared_task
import yfinance as yf
import logging


@shared_task
def fetch_stock_data():
    ticker_symbols = [
        "RELIANCE.NS",
    ]

    for symbol in ticker_symbols:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            # You could save this to a database model
            print(f"{symbol}: {info.get('currentPrice')}")
        except Exception as e:
            logging.error(f"Error fetching data for {symbol}: {e}")
