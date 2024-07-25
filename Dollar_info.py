import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

ticker = 'BRL=X'

finalDateDollar = datetime.today()
initialDateDollar = finalDateDollar - timedelta(days=365*11)

dataDollar = yf.download(ticker,
                         start=initialDateDollar,
                         end=finalDateDollar,
                         interval= '1mo')[
                            'Adj Close'
                         ]