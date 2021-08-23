from celery import shared_task
from . import mail


@shared_task
def send_email(email):
    return mail.order_notification(email)
