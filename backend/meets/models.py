from django.db import models
from django.db.models.base import Model
from datetime import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers
from django.core.mail import EmailMessage
from users.models import NewUser
from django.core.mail import send_mail


def all_emails():
    recievers = []
    for user in NewUser.objects.all():
        recievers.append(user.email)
    return recievers


class Meet(models.Model):
    agenda = models.CharField(max_length=100,)
    # start_time = models.TimeField(default=datetime.now)
    link = models.URLField()
    intiated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='User')

    def save(self, *args, **kwargs):

        super(Meet, self).save()


class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = ('agenda', 'link', 'intiated_by')

    # def create(self, validated_data):
    #     return Meet.objects.create(**validated_data)

    def create(self, validate_data):
        instance = super(MeetSerializer, self).create(validate_data)
        send_mail(
            'HNCC_MANAGEMENT_NOTIFICATION',
            'Hey there a new meet has been scheduled by {username}, Meet link : {LINK} , The agenda of the meet will be {agenda}'.format(
                username=validate_data["intiated_by"], LINK=validate_data["link"], agenda=validate_data["agenda"]),
            'abhinav72610@gmail.com',
            recipient_list=all_emails(),
            fail_silently=False,
        )
        return instance


# def send_email():

#     x = str(MeetSerializer.data["agenda"])
#     z = str(MeetSerializer.data["link"])
#     to = all_emails()
#     email = EmailMessage(
#         'Testing mail',
#         'Hey a new meet has been added',
#         'abhinav72610@gmail.com',
#         to=to
#     )
#     email.send()
#     print(str(MeetSerializer.validated_data))


# @receiver(post_save, sender=Meet)
# def send_mail_on_create(sender, instance=None, created=False, **kwargs):
#     if created:
#         send_email()  # call send mail function

#  "hey a new meet has been added ,agenda of the meet is" +
#         " " + x + "link is"+" " + z + "Thanks",
