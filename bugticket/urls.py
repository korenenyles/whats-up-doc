from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeView, name='home'),
    path('signup/', views.signUpView, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ticket_detail/<int:id>', views.ticket_detail, name='ticket_detail'),
]
