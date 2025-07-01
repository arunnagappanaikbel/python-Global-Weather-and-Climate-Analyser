# src/logger.py

import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_path="data/logs/pipeline.log"):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            RotatingFileHandler(log_path, maxBytes=10**6, backupCount=3),
            logging.StreamHandler()
        ],
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
