import streamlit as st
import pandas as pd
import os
from src.fetch_data import fetch_yahoo_data  # Daten abrufen, falls nötig

# Titel des Dashboards
st.title("📈 Finanzdaten Dashboard")

# Aktien-Ticker
ticker = "AAPL"
data_path = f"data/{ticker}_data.csv"

# Prüfen, ob Datei existiert – falls nicht, Daten abrufen
if not os.path.exists(data_path):
    st.warning("⚠️ Daten nicht gefunden! Abrufe Finanzdaten...")
    df = fetch_yahoo_data(ticker)
    df.to_csv(data_path, index=False)
    st.success("✅ Daten erfolgreich geladen!")

# CSV-Datei einlesen & falsche Header-Zeilen entfernen
df = pd.read_csv(data_path, skiprows=2)  # Erste 2 Zeilen überspringen

# Automatisch den Index setzen (Datum)
df.rename(columns={"Price": "Date"}, inplace=True)  # Richtige Spalte benennen
df.set_index("Date", inplace=True)
df.index = pd.to_datetime(df.index)  # Sicherstellen, dass es ein Datum ist

# Preisentwicklung anzeigen
st.subheader(f"Aktienkurs von {ticker} über die Zeit")
st.line_chart(df["Close"])

# Tägliche Renditen anzeigen
st.subheader("Histogramm der täglichen Renditen")
df["Daily_Return"] = df["Close"].pct_change()
st.bar_chart(df["Daily_Return"].dropna())

st.write("🚀 Dieses Dashboard aktualisiert sich automatisch mit GitHub Actions!")
