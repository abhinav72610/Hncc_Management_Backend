# Generated by Django 3.2.4 on 2021-07-09 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('team', models.CharField(choices=[('web', 'WEB'), ('mobile', 'MOBILE'), ('design', 'DESIGN'), ('game', 'GAME')], default='web', max_length=10)),
                ('content', models.CharField(max_length=300)),
                ('start_date', models.DateTimeField()),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]