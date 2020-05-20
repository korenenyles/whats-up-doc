from django.contrib import admin
from bugticket.models import CustomUser, Ticket
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Ticket)