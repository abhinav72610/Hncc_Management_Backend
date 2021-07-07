from django.urls import path
from .views import MeetView
urlpatterns = [


    path('', MeetView.as_view(), name='Meetview'),
]
