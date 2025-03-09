# src/fetch_data.py
import yfinance as yf
import pandas as pd

def fetch_yahoo_data(ticker: str, start="2023-01-01", end="2024-01-01"):
    """
    Ruft historische Daten von Yahoo Finance für ein gegebenes Ticker-Symbol ab.
    
    :param ticker: Aktien-Symbol (z.B. "AAPL" für Apple)
    :param start: Startdatum (YYYY-MM-DD)
    :param end: Enddatum (YYYY-MM-DD)
    :return: Pandas DataFrame mit den Finanzdaten
    """
    data = yf.download(ticker, start=start, end=end)
    return data

if __name__ == "__main__":
    df = fetch_yahoo_data("AAPL")
    print(df.head())  # Zeigt die ersten Zeilen der Daten
