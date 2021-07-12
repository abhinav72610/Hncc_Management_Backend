from django.db.models.expressions import F
from rest_framework import serializers
from .models import Events
from users.models import NewUser, Profile
from django.core.mail import send_mail


def all_emails(team):
    recievers = []
    for User in Profile.objects.filter(expertise=team):
        recievers.append(User.user.email)
    return recievers


class Eventserializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'lead', 'team', 'content', 'start_date')
        model = Events

    def create(self, validate_data):
        instance = super(Eventserializer, self).create(validate_data)
        send_mail(
            'HNCC_MANAGEMENT_NOTIFICATION',
            'Hey there a new event has been scheduled by {username}, titled : {title} , The content of the event will be {agenda}'.format(
                username=validate_data["lead"], title=validate_data["title"], agenda=validate_data["content"]),
            'abhinav72610@gmail.com',
            recipient_list=all_emails(validate_data['team']),
            fail_silently=False,
        )
        return instance
