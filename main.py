import pandas as pd
import numpy as np
import os
import logging
from datetime import datetime
from src.config_loader import load_config
from src.logger import setup_logger
from src.fetch.fetch_weather_api import fetch_daily_weather
from src.process.clean_transform import clean_weather_data
from src.process.analysis import detect_temperature_outliers, summarize_climate

def main():
    config = load_config()
    setup_logger()
    logger = logging.getLogger(__name__)
    
    start = config['defaults']['start_date']
    end = config['defaults']['end_date']
    coordinates = config['defaults']['coordinates']
    
    all_weather = []
    
    #Extract
    for coord in coordinates:
        df = fetch_daily_weather(coord['lat'],coord['lon'],start,end)
        df_clean = clean_weather_data(df)#Transformation
        all_weather.append(df_clean)
        
    weather_df = pd.concat(all_weather, ignore_index=True)
    
    #Analysis
    weather_df = detect_temperature_outliers(weather_df)
    summary_df = summarize_climate(weather_df)
    
    #Load
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs("output/insights", exist_ok=True)
    
    weather_df.to_csv(f'output/insights/weather_data_{today}.csv', index=False)
    summary_df.to_csv(f'output/insights/climate_summary_{today}.csv', index=False)
    
    print("✅ ETL pipeline executed successfully.")
    logger.info(f'ETL completed succesfully')    
    
       
if __name__ == '__main__':
    main()

