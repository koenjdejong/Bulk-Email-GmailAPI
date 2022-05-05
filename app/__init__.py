import logging
from datetime import datetime
import os
from app.config import Config, ConfigError

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
    from app.mail import send_message
    attachments = test()
    if len(attachments) == 1:
        logging.info("No attachments found.")
    recipients = config["recipients"]
    logging.info(f"Sending email to {len(recipients)} recipients.")

    for recipient in recipients:
        send_message(recipient, attachments)

def test():
    if not (os.path.exists("templates") and os.path.isdir("templates")):
        os.mkdir("templates")
        logging.info("Created templates directory.")

    all_files = []
    for root, dirs, files in os.walk("templates"):
        for file in files:
            all_files.append(f"{root}/{file}")

    if len(all_files) == 0 or f"templates/{config['template_file']}" not in all_files:
        logging.info("Creating template...")
        with open(f"templates/{config['template_file']}", "w"):
            raise ConfigError("No template found. An empty template file has been created for you")

    if len(all_files) != len(set(all_files)):
        logging.info("Duplicate template files found.")
        raise ConfigError("Duplicate template files found.")

    return all_files
