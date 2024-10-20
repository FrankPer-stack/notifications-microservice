
from email.utils import formataddr

from config import get_settings
from fastapi import HTTPException
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Attachment, Mail


def send(
    sender,
    recipient,
    subject,
    html_content,
):     
    message = Mail(
        from_email=formataddr(("Koloni", sender)),
        to_emails=recipient,
        subject=subject,
        html_content=html_content,
    )
    sg = SendGridAPIClient(api_key=get_settings().twilio_sendgrid_api_key)

    try:
        sg.send(message)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="There was an error trying to send an email to the user with the email address provided. This incident has been reported.",
        )

