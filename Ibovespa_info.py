import yfinance as yf
import pandas as pd

from datetime import timedelta, datetime

ticker = '^BVSP'

finalDate = datetime.today()
initialDate = finalDate - timedelta(days=365*11)

data = yf.download(ticker,
                   start=initialDate,
                   end=finalDate,
                   interval='1mo')[
                        'Adj Close'
                    ]
