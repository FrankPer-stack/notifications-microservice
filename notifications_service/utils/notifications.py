import logging
from abc import ABC, abstractmethod
from typing import List
from config import get_settings
from twilio.rest import Client
from utils import email
from models import UserRecipient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
settings = get_settings()


class NotificationStrategy(ABC):
    """Abstract base class for notification strategies."""
    @abstractmethod
    async def send(self, recipient: UserRecipient, message: str):
        pass


class EmailNotification(NotificationStrategy):
    """Concrete Email notification strategy."""

    async def send(self, recipient: UserRecipient, message: str) -> dict:
        logger.info(f"Email message: {message}")
        email_sender = get_settings().twilio_sendgrid_auth_sender
        email.send(
            email_sender,
            recipient.email,
            "notification",
            message,
        )
        return {"status": "sent"}


class SMSNotification(NotificationStrategy):
    """Concrete SMS notification strategy."""

    async def send(self, recipient: UserRecipient, message: str) -> dict:
        logger.info(f"SMS message: {message}")
        sid = get_settings().twilio_phone_number
        client = Client(
            username=get_settings().twilio_sid, password=get_settings().twilio_secret
        )
        client.messages.create(to=recipient.phone, from_=sid, body=message)
        return {"status": "sent"}


class NotificationManager:
    """Manages sending notifications via different channels."""

    def __init__(self):
        self.strategies = {
            "email": EmailNotification(),
            "sms": SMSNotification(),
        }

    async def send_notification(
        self, channels: List[str], recipient: UserRecipient, message: str
    ) -> dict:
        for channel in channels:
            strategy = self.strategies.get(channel)
            if strategy:
                await strategy.send(recipient, message)
            else:
                logger.warning(f"Channel '{channel}' not supported.")


class MessagingService:
    """Service for managing messaging actions (email, SMS, push, etc.)."""

    def __init__(self):
        self.notification_manager = NotificationManager()

    async def send_notification(
        self, channels: List[str], recipient: UserRecipient,  message: str
    ) -> dict:
        """Send notifications via different channels."""
        logger.info(f"channels:{channels}")
        logger.info(f"recipient:{recipient}")
        logger.info(f"message:{message}")
        return await self.notification_manager.send_notification(channels, recipient, message)