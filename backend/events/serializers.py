from django.db.models.expressions import F
from rest_framework import serializers
from .models import Events


class Eventserializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'lead', 'team', 'content', 'start_date')
        model = Events
