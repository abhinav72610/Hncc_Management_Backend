from rest_framework import serializers
from .models import Meet


class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = ('agenda', 'start_time', 'link', 'intiated_by')
