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

**🔧 Key Features & Workflow**
**1. Real-Time Multi-Source Data Ingestion**
 - Pull current and historical weather from Meteostat API
 - Nested JSON from OpenWeather Air Pollution API
 - Load historical temperature/precipitation from complex CSV (e.g., NOAA or NASA)

**2. Data Parsing & Complex Transformation**
 - Parse multi-nested JSON and flatten for analysis
 - Handle mixed and missing formats (nulls, dtypes, nested fields)
- Merge data from multiple APIs and historical files
- Time zone normalization, rolling averages, lag analysis
- Correlation, trend analysis, anomaly detection using NumPy

**3. Analysis Module**
 - Identify patterns in weather changes for cities/stations
 - Detect extreme conditions using NumPy thresholds
 - Create pivot tables, plots, and summary statistics
 - Generate city-wise and region-wise climate reports

**4. Logging & Error Handling**
 - Use logging with rotation and custom format
 - Gracefully handle API failures, file parsing errors, etc.
 - Exception handling for type errors, missing fields, malformed data

**5. Configuration Management**
 - Use config.yaml and .env for storing API keys, endpoints, file paths
