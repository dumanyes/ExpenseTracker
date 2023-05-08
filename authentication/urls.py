from .views import RegistertrationView
from django.urls import path


urlpatterns = [

    path('register', RegistertrationView.as_view(), name='register')
]