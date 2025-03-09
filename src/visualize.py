# src/visualize.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_stock_prices(df: pd.DataFrame, ticker: str):
    """
    Erstellt ein Liniendiagramm für den Aktienkurs.

    :param df: Pandas DataFrame mit Finanzdaten
    :param ticker: Aktien-Ticker für Titel der Grafik
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Schlusskurs", linewidth=2)
    plt.plot(df.index, df["MA_50"], label="50-Tage MA", linestyle="--")
    plt.plot(df.index, df["MA_200"], label="200-Tage MA", linestyle="--")
    
    plt.title(f"Aktienkurs von {ticker}")
    plt.xlabel("Datum")
    plt.ylabel("Preis in USD")
    plt.legend()
    plt.grid()
    plt.show()

def plot_daily_returns(df: pd.DataFrame):
    """
    Erstellt ein Histogramm der täglichen Renditen.

    :param df: Pandas DataFrame mit Finanzdaten
    """
    plt.figure(figsize=(10, 5))
    sns.histplot(df["Daily_Return"].dropna(), bins=50, kde=True)
    plt.title("Histogramm der täglichen Renditen")
    plt.xlabel("Tägliche Rendite")
    plt.ylabel("Häufigkeit")
    plt.show()

if __name__ == "__main__":
    from fetch_data import fetch_yahoo_data
    from preprocess import preprocess_data
    from analysis import calculate_moving_averages

    # Daten abrufen & vorbereiten
    df = fetch_yahoo_data("AAPL")
    clean_df = preprocess_data(df)
    clean_df = calculate_moving_averages(clean_df)

    # Visualisierungen
    plot_stock_prices(clean_df, "AAPL")
    plot_daily_returns(clean_df)
