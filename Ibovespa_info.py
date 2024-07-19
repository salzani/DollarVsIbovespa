import yfinance as yf
import pandas as pd

ticker = '^BVSP'

data = yf.download(ticker, start='2023-01-01', end='2024-01-01', interval='1mo')

ibovespaData = data.loc['2023-01-01':'2023-12-31']
