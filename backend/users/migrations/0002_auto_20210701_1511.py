# Generated by Django 3.2.4 on 2021-07-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='year',
        ),
        migrations.AddField(
            model_name='newuser',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
