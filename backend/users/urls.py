from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, Users_year

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('', Users_year.as_view(), name="Users_2k19")
]
