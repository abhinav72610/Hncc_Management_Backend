from rest_framework import generics
from .models import Meet, MeetSerializer


class MeetView(generics.ListCreateAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer
