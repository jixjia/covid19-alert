from twilio.rest import Client
from . import config


class SMSNotification:
    def __init__(self):
        self.client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)

    def send(self, sms_to, sms_body):
        message = self.client.messages.create(
            from_=config.FROM_,
            body=sms_body,
            to=sms_to
        )
        return message.sid
