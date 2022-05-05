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
    body, attachments = test_templates()
    if len(attachments) == 1:
        logging.info("No attachments found.")
    recipients = config["recipients"]
    logging.info(f"Sending email to {len(recipients)} recipients.")

    body = open(body, "r").read()
    subject = config["subject"]

    if config["test"]:
        logging.info("Sending test email...")
        send_message(config["test_email_recipient"], subject, body, attachments)
        logging.info("Test email sent.")
        return

    for recipient in recipients:
        send_message(recipient, subject, body, attachments)
        logging.info(f"Email sent to {recipient}.")


def test_templates():
    if not (os.path.exists("templates") and os.path.isdir("templates")):
        os.mkdir("templates")
        logging.info("Created templates directory.")

    all_files = []
    body = None
    for root, dirs, files in os.walk("templates"):
        for file in files:
            if file == config["template_file"]:
                body = f"{root}/{file}"
            else:
                all_files.append(f"{root}/{file}")

    if not body:
        logging.error(f"Template {config['template']} not found.")
        logging.info("Creating template...")
        with open(f"templates/{config['template_file']}", "w"):
            raise ConfigError("No template found. An empty template file has been created for you")

    if len(all_files) != len(set(all_files)):
        logging.info("Duplicate template files found.")
        raise ConfigError("Duplicate template files found.")

    return body, all_files
