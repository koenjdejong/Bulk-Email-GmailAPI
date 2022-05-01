import logging
from datetime import datetime
import os
from config import Config

if not (os.path.exists('log') or os.path.isdir('log')):
    os.mkdir('log')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(f"log/LOG_{str(datetime.now()).replace(' ', '_')}.log"), logging.StreamHandler()])

config = Config("config.json")
logging.info(f"Config loaded.")


def start():
    """ Start the application """
    logging.info("Starting...")
