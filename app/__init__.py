import logging
from datetime import datetime
import os

if not (os.path.exists('log') or os.path.isdir('log')):
    os.mkdir('log')


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(f"log/LOG_{str(datetime.now()).replace(' ', '_')}.log"), logging.StreamHandler()])


def start():
    logging.info("Starting...")