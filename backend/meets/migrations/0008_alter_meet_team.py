# Generated by Django 3.2.4 on 2021-07-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0007_auto_20210719_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='team',
            field=models.CharField(choices=[('web', 'WEB'), ('mobile', 'MOBILE'), ('design', 'DESIGN'), ('game', 'GAME'), ('all', 'ALL')], default='design', max_length=10),
        ),
    ]
