from django.db import models
from django.conf import settings

# Create your models here.


class Tasks(models.Model):

    title = models.CharField(max_length=100)
    asigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_to')

    content = models.CharField(max_length=300)
    start_date = models.DateTimeField()
