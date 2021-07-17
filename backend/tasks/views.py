from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import Taskserializer
from rest_framework import permissions
from users.models import NewUser


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


class TasksView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Tasks.objects.all()
    serializer_class = Taskserializer


class get_user_tasks(generics.RetrieveUpdateAPIView):
    serializer_class = Taskserializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        id = self.kwargs['pk']
        # user = NewUser.objects.filter(id=id)
        # username = user.user_name

        return Tasks.objects.filter(asigned_to=id)
