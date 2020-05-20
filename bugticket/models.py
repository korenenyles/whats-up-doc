from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    display_name = models.CharField(max_length = 50)

class Ticket(models.Model):
    #https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
    NEW = 'NEW'
    IN_PROGRESS = 'IN PROGRESS'
    DONE = 'DONE'
    INVALID = 'INVALID'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]

    title = models.CharField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    filed_user = models.ForeignKey(get_user_model(),related_name='filed_user', on_delete=models.CASCADE) 
    ticket_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=NEW,)
    assigned_user = models.ForeignKey(get_user_model(),related_name='assigned_user', on_delete=models.CASCADE)
    completed_user = models.ForeignKey(get_user_model(),related_name='completed_user', on_delete=models.CASCADE)
    #Peter Marsh assisted with fixing the related names to actually makemigrations
    
    def __str__(self):
        return self.title