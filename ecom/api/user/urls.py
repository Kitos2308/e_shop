from rest_framework import routers
from django.urls import path, include

from .views import *


urlpatterns =[
path('register', RegisterApiView.as_view()),
    path('login', LoginApiView.as_view()),
    path('user', UserAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('authme', CheckAuthUser.as_view()),
]