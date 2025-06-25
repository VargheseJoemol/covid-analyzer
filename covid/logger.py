import logging
import sys
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

def get_logger(name: str = "covid-analyzer") -> logging.Logger:
    logger = logging.getLogger(name)

    # Read log config from env vars
    log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
    log_to_file = os.getenv("LOG_TO_FILE", "true").lower() == "true"
    log_file_path = Path(os.getenv("LOG_FILE", "covid.log"))

    logger.setLevel(getattr(logging, log_level, logging.DEBUG))

    # Prevent duplicate handlers on re-import
    if not logger.handlers:
        # Console Handler (colored optional)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
        ))
        logger.addHandler(stream_handler)

        # Optional: Rotating File Handler
        if log_to_file:
            file_handler = RotatingFileHandler(
                filename=log_file_path,
                maxBytes=1_000_000,  # 1MB
                backupCount=3        # keep 3 old logs
            )
            file_handler.setFormatter(logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
            ))
            logger.addHandler(file_handler)

    return logger

