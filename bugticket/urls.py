from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeView, name='home'),
    path('signup/', views.signUpView, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ticket_detail/<int:id>', views.ticket_detail, name='ticket_detail'),
    path('create_ticket/<int:user_id>', views.create_ticket, name='create_ticket'),
    path('inprogress/edit/<int:ticket_id>', views.inprogress_ticket, name="in_progress"),
    path('completed/edit/<int:ticket_id>', views.complete_ticket, name="done"),
    path('invalid/edit/<int:ticket_id>', views.invalid_ticket, name="invalid"),
    path('edit_ticket/edit/<int:ticket_id>', views.edit_ticket, name='edit'),
    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),
    
]