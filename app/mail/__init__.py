from app.mail.authentication import authenticate
from app.mail.message import build_message
import logging

mail_service = authenticate()


def send_message(destination, obj, body, attachments=None):
    logging.info(f"Sending message to {destination}")
    return mail_service.users().messages().send(userId="me", body=build_message(destination, obj, body, attachments)).execute()
