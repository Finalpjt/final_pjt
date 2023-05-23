from django.urls import path
from .views import user_list, user_detail, user_nickname

urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('users/<int:id>', user_detail, name='user-detail'),
    path('users/nickname', user_nickname, name='user-nickname')
]
