from django.urls import path
from .views import *
urlpatterns = [
    path('users',UserSignUp.as_view()),
]
