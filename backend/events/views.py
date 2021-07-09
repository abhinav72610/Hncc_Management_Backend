from django.shortcuts import render
from rest_framework import generics
from .models import Events
from .serializers import Eventserializer


class EventsView(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = Eventserializer
