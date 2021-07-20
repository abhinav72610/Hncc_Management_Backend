from django.db import models
from django.conf import settings

# Create your models here.


class Events(models.Model):
    # id*
    # title*
    # content*
    # start_date*
    # announcement_date*
    # lead
    # team [:connection -> teams]
    # guests*
    # type
    # category
    # sponsors
    # assets
    options = (
        ('web', 'WEB'),
        ('mobile', 'MOBILE'),
        ('design', 'DESIGN'),
        ('game', 'GAME'),
        ('marketing', 'MARKETING'),

    )
    title = models.CharField(max_length=100)
    lead = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    team = models.CharField(
        max_length=10, choices=options, default='web')
    content = models.CharField(max_length=300)
    start_date = models.DateTimeField()
