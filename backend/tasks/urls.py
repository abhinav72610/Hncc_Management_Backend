from django.urls import path
from .views import TasksView, get_user_tasks
urlpatterns = [


    path('', TasksView.as_view(), name='Tasksview'),
    path('task/<int:pk>/', get_user_tasks.as_view(),
         name="get_user_task")
]
