import logging

from celery import shared_task
from django.urls import reverse
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import get_user_model
# from proj_celery.celery import app
import time

from proj_celery.celery import app
from .models import Example


@shared_task
def send_verification_mail(sms):
    print(sms)
    email = EmailMessage(
        'test', sms, 'wambua.eric01@gmail.com', ['wambua.eric01@gmail.com']
    )
    try:
        r = email.send()
        print(f'send{r}')
    except Exception as e:
        print(f'error, {e}')
