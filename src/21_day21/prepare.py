import yfinance as yf

tsm = yf.download("TSM", start="2019-01-01", end="2024-09-01", interval="1mo")

tsm.to_csv("tsm.csv")
