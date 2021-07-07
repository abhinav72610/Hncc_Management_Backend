from rest_framework import viewsets
from .models import Meet
from .serializers import MeetSerializer
from django.core.mail import EmailMessage
from rest_framework import generics


class MeetView(generics.ListCreateAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer


def send_email(request):
    email = EmailMessage(
        'Title',
        (MeetSerializer.agenda, MeetSerializer.start_time, MeetSerializer.link),
        'my-email',
        ['my-receive-email']
    )
    email.send()
