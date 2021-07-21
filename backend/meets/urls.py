from django.urls import path
from .views import MeetView, IndividualMeetView
urlpatterns = [


    path('', MeetView.as_view(), name='Meetview'),
    path('meet/<int:pk>/', IndividualMeetView.as_view(),
         name="IndividualMeetView")
]
