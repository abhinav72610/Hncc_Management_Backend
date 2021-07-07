from re import I
from django.db import models
from django.db.models.base import Model
from datetime import datetime
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .views import send_email

# Create your models here.


class Meet(models.Model):
    agenda = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    link = models.URLField()
    intiated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='User')

# @receiver(post_save, sender=Meet)
# def send_mail_on_create(sender, instance=None, created=False, **kwargs):
#     if created:
#         send_email() # call send mail function
