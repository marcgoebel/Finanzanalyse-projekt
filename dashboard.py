import streamlit as st
import pandas as pd
import os
from src.fetch_data import fetch_yahoo_data  # Falls Daten fehlen

# Titel des Dashboards
st.title("📈 Finanzdaten Dashboard")

# Aktien-Ticker
ticker = "AAPL"
data_path = f"data/{ticker}_data.csv"

# Prüfen, ob Datei existiert – falls nicht, abrufen
if not os.path.exists(data_path):
    st.warning("⚠️ Daten nicht gefunden! Abrufe Finanzdaten...")
    df = fetch_yahoo_data(ticker)
    df.to_csv(data_path, index=False)
    st.success("✅ Daten erfolgreich geladen!")

# CSV einlesen – richtige Header-Zeile setzen
df = pd.read_csv(data_path, skiprows=3)  # Erste drei Zeilen überspringen

# Prüfen, ob die richtigen Spalten geladen wurden
st.write("📊 Verfügbare Spalten:", df.columns.tolist())

# Falls "Close" nicht existiert, alternative Namen suchen
if "Close" not in df.columns:
    for col in df.columns:
        if "close" in col.lower():
            df.rename(columns={col: "Close"}, inplace=True)

# Sicherstellen, dass "Close" jetzt existiert
if "Close" in df.columns:
    st.subheader(f"Aktienkurs von {ticker} über die Zeit")
    st.line_chart(df["Close"])
else:
    st.error("⚠️ Spalte 'Close' wurde nicht gefunden! Überprüfe die CSV-Datei.")

# Datum setzen
if "Date" in df.columns:
    df.set_index("Date", inplace=True)
    df.index = pd.to_datetime(df.index)

# Tägliche Renditen anzeigen
if "Close" in df.columns:
    st.subheader("Histogramm der täglichen Renditen")
    df["Daily_Return"] = df["Close"].pct_change()
    st.bar_chart(df["Daily_Return"].dropna())

st.write("🚀 Dieses Dashboard aktualisiert sich automatisch mit GitHub Actions!")
