from rest_framework import serializers
from .models import Tasks


class Taskserializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'asigned_to', 'content', 'start_date')
        model = Tasks
