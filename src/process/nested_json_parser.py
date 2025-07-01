# src/process/nested_json_parser.py

import json
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def flatten_json(y):
    """
    Recursively flattens a nested JSON object.
    """
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, f'{name}{i}_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def parse_air_quality_json(json_data):
    """
    Parse multi-nested JSON from OpenWeather Air Quality API into DataFrame.
    """
    try:
        flattened = [flatten_json(entry) for entry in json_data.get('list', [])]
        df = pd.DataFrame(flattened)
        logger.info(f"Parsed {len(df)} air quality records.")
        return df
    except Exception as e:
        logger.exception("Failed to parse air quality JSON.")
        return pd.DataFrame()


def parse_climate_zones_json(file_path):
    """
    Parse a local climate_zones.json file into a structured DataFrame.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        records = []
        for region, zones in data.items():
            for zone, cities in zones.items():
                for city in cities:
                    records.append({"region": region, "zone": zone, "city": city})

        df = pd.DataFrame(records)
        logger.info(f"Parsed climate zones for {len(df)} cities.")
        return df
    except Exception as e:
        logger.exception("Failed to parse climate zones JSON.")
        return pd.DataFrame()
