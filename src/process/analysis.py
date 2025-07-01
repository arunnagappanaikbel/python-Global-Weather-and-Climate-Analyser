# src/process/analysis.py

import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def summarize_climate(df):
    """
    Generate summary statistics and anomalies for weather data.
    """
    try:
        summary = df.groupby('location').agg({
            'tavg': ['mean', 'std', 'min', 'max'],
            'prcp': ['sum', 'mean'],
            'temp_range': 'mean'
        }).reset_index()

        summary.columns = ['_'.join(col).strip('_') for col in summary.columns.values]
        logger.info("Climate summary computed.")
        return summary
    except Exception as e:
        logger.exception("Error summarizing climate data.")
        return pd.DataFrame()


def detect_temperature_outliers(df):
    """
    Detect extreme outliers in temperature using IQR.
    """
    try:
        Q1 = df['tavg'].quantile(0.25)
        Q3 = df['tavg'].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df['temp_outlier'] = ((df['tavg'] < lower_bound) | (df['tavg'] > upper_bound))
        logger.info(f"Outlier detection complete: {df['temp_outlier'].sum()} outliers found.")
        return df
    except Exception as e:
        logger.exception("Failed in outlier detection.")
        return df
