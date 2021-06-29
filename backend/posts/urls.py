from django.urls import path
from .views import PostList, PostDetail
urlpatterns = [
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/post/<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('api/posts', PostList.as_view(), name='listcreate'),
]
