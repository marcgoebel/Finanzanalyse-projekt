# src/analysis.py

import pandas as pd
import statsmodels.api as sm

def calculate_moving_averages(df: pd.DataFrame, short_window=50, long_window=200):
    """
    Berechnet gleitende Durchschnitte für die Aktienkurse.

    :param df: Pandas DataFrame mit Finanzdaten
    :param short_window: Zeitraum für den kurzfristigen Durchschnitt (z.B. 50 Tage)
    :param long_window: Zeitraum für den langfristigen Durchschnitt (z.B. 200 Tage)
    :return: DataFrame mit zusätzlichen Spalten für MA
    """
    df[f"MA_{short_window}"] = df["Close"].rolling(window=short_window).mean()
    df[f"MA_{long_window}"] = df["Close"].rolling(window=long_window).mean()
    return df

def run_arima_model(df: pd.DataFrame):
    """
    Führt eine einfache ARIMA-Zeitreihenanalyse durch.

    :param df: Pandas DataFrame mit Finanzdaten
    :return: ARIMA-Modellzusammenfassung
    """
    df = df.dropna()  # Fehlende Werte entfernen
    model = sm.tsa.ARIMA(df["Close"], order=(5, 1, 0))  # ARIMA(5,1,0)
    results = model.fit()
    return results.summary()

if __name__ == "__main__":
    from fetch_data import fetch_yahoo_data
    from preprocess import preprocess_data

    # Daten abrufen & vorbereiten
    df = fetch_yahoo_data("AAPL")
    clean_df = preprocess_data(df)

    # Gleitende Durchschnitte berechnen
    clean_df = calculate_moving_averages(clean_df)

    # ARIMA-Modell ausführen
    arima_results = run_arima_model(clean_df)
    
    print(clean_df.head())  # Zeigt Daten mit Moving Averages
    print(arima_results)  # Zeigt ARIMA-Modell-Zusammenfassung
