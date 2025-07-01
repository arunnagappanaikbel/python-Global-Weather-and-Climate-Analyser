import requests
import pandas as pd
import logging
import datetime
from src.config_loader import load_config


logger = logging.getLogger(__name__)
config = load_config()

def fetch_daily_weather(lat,long,start,end):
    """
    fetch daily weather data for a given location and date range using meteostat API
    """
    try:       
        url = "https://meteostat.p.rapidapi.com/point/monthly"

        querystring = {"lat":lat,"lon":long,"alt":"43","start":start,"end":end}

        headers = {
	        "x-rapidapi-key": config["api_keys"]["meteostat"],
	        "x-rapidapi-host": "meteostat.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if "data" not in data:
            logger.error(f'No data field in API response: {data}')
            
        df = pd.DataFrame(data["data"])
        df['date'] = pd.to_datetime(df['date'])
        df['location'] = f"{lat},{long}"
        logger.info(f'fetched {len(df)} records for {lat}, {long} from {start} to {end} ')
        
        return df
        
        
    except requests.exceptions.RequestException as e:
        logger.exception(f'request failed for {lat}, {long} from {start} to {end}')