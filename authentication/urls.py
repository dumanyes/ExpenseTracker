
from django.urls import path

from authentication import views

urlpatterns = [


    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('index/', views.HomePage, name='index'),
    path('logout/', views.LogoutPage, name='logout'),


]