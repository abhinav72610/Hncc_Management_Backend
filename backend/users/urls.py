from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, Users_year, User_profile, Other_user_profiles

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('', Users_year.as_view(), name="Users_2k19"),
    path('profile/', User_profile.as_view(), name="User_profile"),
    path('profile/<int:pk>/', Other_user_profiles.as_view(),
         name="Other_users_profile")
]
