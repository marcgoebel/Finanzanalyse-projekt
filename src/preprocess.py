# src/preprocess.py

import pandas as pd

def preprocess_data(df: pd.DataFrame):
    """
    Bereitet die Finanzdaten auf:
    - Entfernt fehlende Werte
    - Berechnet tägliche Renditen
    - Formatiert Spaltennamen
    
    :param df: Rohdaten als Pandas DataFrame
    :return: Bereinigter DataFrame
    """
    
    # Fehlende Werte entfernen
    df = df.dropna()

    # Spalten umbenennen (z. B. für Klarheit)
    df = df.rename(columns={"Adj Close": "Adjusted_Close"})

    # Tägliche Rendite berechnen
    df["Daily_Return"] = df["Close"].pct_change()

    return df

if __name__ == "__main__":
    from fetch_data import fetch_yahoo_data

    df = fetch_yahoo_data("AAPL")
    clean_df = preprocess_data(df)
    
    print(clean_df.head())  # Erste Zeilen ausgeben
