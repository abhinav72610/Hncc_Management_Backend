from django.urls import path
from .views import get_user_tasks, get_tasks
urlpatterns = [


    path('', get_user_tasks.as_view(), name='Tasksview'),
    path('task/<int:pk>/', get_tasks.as_view(),
         name="get tasks")


]
