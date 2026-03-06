import logging
import os

LOG_DIR = "logs"
LOG_FILE = "logs/trading.log"

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    logger = logging.getLogger()
    return logger