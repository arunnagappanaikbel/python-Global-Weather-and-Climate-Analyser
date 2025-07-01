import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def clean_weather_data(df):
    """
    clean and transform raw weather data from API
    """
    try:
        if df.empty:
            logger.warning(f'Received data frame is empty')
            return

        # fill missing values
        df = df.fillna({
            'tavg':df['tavg'].mean(),
            'tmin':df['tmin'].mean(),
            'tmax':df['tmax'].mean(),
            'prcp':0,
            'wspd':df['wspd'].median()
        })
        
        #calculate additional features
        df['temp_range'] = df['tmax'] - df['tmin']
        df['7d_avg_temp'] = df['tavg'].rolling(window=7, min_periods=1).mean()
        
        #anomoly detection
        mean = np.mean(df['tavg'])
        std = np.std(df['tavg'])
        df['is_anomaly'] = np.where((df['tavg'] > mean + 2 * std) |
                                    (df['tavg'] < mean - 2 * std), True, False)
        
        logger.info(f'data cleaned and transformed successfuly')
        return df
        
    except Exception as e:
        logger.error(f'failed during transform raw weather data')