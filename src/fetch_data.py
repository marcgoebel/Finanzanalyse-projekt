import yfinance as yf
import pandas as pd
import os

def fetch_yahoo_data(ticker: str, start="2023-01-01", end="2024-12-31"):
    """
    Ruft historische Daten von Yahoo Finance ab und speichert sie als CSV.
    """
    data = yf.download(ticker, start=start, end=end)

    # 🔥 Explizit prüfen, ob das Verzeichnis existiert, und es anlegen
    data_folder = "data"

    try:
        os.makedirs(data_folder, exist_ok=True)
        print(f"✅ Ordner '{data_folder}' wurde erfolgreich erstellt oder existiert bereits.")
    except Exception as e:
        print(f"❌ Fehler beim Erstellen des Ordners '{data_folder}': {e}")

    # Speichern als CSV
    csv_path = os.path.join(data_folder, f"{ticker}_data.csv")

    try:
        data.to_csv(csv_path)
        print(f"✅ Daten gespeichert unter: {csv_path}")
    except Exception as e:
        print(f"❌ Fehler beim Speichern der Datei: {e}")

    return data

if __name__ == "__main__":
    df = fetch_yahoo_data("AAPL")
    print(df.head())
