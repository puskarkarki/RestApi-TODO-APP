from todo.views import ListTodo
from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Todo)
