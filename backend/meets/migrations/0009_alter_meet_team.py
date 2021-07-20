# Generated by Django 3.2.4 on 2021-07-20 05:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0008_alter_meet_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='team',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('web', 'WEB'), ('mobile', 'MOBILE'), ('design', 'DESIGN'), ('game', 'GAME'), ('all', 'ALL')], default='design', max_length=26),
        ),
    ]
