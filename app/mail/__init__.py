from app.mail.authentication import authenticate
from app.mail.message import build_message
import logging

authenticate()


def send_message(service, destination, obj, body, attachments=None):
    logging.info(f"Sending message to {destination}")
    # return service.users().messages().send(userId="me", body=build_message(destination, obj, body, attachments)).execute()
