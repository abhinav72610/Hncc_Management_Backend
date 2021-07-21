from rest_framework import generics
from .models import Meet, MeetSerializer, Meet_2_Serializer
from rest_framework.permissions import IsAdminUser
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


class MeetView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer


class IndividualMeetView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Meet_2_Serializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return Meet.objects.filter(id=id)
