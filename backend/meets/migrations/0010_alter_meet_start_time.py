# Generated by Django 3.2.4 on 2021-07-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0009_alter_meet_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
