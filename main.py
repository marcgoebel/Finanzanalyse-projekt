# main.py
# Hauptskript für Finanzanalyse-Projekt

from src.fetch_data import fetch_yahoo_data
from src.preprocess import preprocess_data
from src.analysis import perform_analysis
from src.visualize import plot_data

def main():
    # 1. Daten abrufen
    raw_data = fetch_yahoo_data("AAPL")
    
    # 2. Daten aufbereiten
    clean_data = preprocess_data(raw_data)
    
    # 3. Analysen durchführen
    analysis_results = perform_analysis(clean_data)
    
    # 4. Visualisierung
    plot_data(clean_data)
    
if __name__ == "__main__":
    main()
