**✅ Project Title: Global Weather & Climate Pattern Analyzer**
**🧠 Overview:**
This project fetches real-time and historical weather data from multi-nested APIs and CSV/JSON sources, performs complex data transformations, aggregation, statistical modeling (with NumPy), and produces analytical insights and alerts.

**we used :**

- Real-time weather APIs (like Open-Meteo, WeatherAPI, or Meteostat)
- Multi-nested JSON from API (climate zones, air quality, etc.)
- Complex CSV files (e.g., NASA GISTEMP, NOAA datasets)
- NumPy for numerical computations
- pandas for manipulation and ETL
- Logging, error handling, configuration, modular code


## 📂 Repository Structure
```
weather_climate_analyzer/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── logs/
│
├── inputs/
│   ├── stations.csv
│   └── climate_zones.json
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config_loader.py
│   ├── logger.py
│   ├── fetch/
│   │   ├── __init__.py
│   │   ├── fetch_weather_api.py
│   │   └── fetch_csv_json.py
│   ├── process/
│   │   ├── __init__.py
│   │   ├── clean_transform.py
│   │   ├── nested_json_parser.py
│   │   └── analysis.py
│   └── utils/
│       └── helpers.py
│
├── output/
│   └── insights/
│       └── climate_summary.csv
│
├── .env
├── requirements.txt
└── README.md
```
---
