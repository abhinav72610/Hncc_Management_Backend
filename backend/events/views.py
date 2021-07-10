from django.shortcuts import render
from rest_framework import generics
from .models import Events
from .serializers import Eventserializer
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # if request.method in ['list', 'retrieve']:
        #     return True

        # elif request.method in ['create']:
        #     return request.user.is_authenticated() and request.user.is_admin
        # # else:
        # #     return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class EventsView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Events.objects.all()
    serializer_class = Eventserializer
