from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name='register'),
    path('log/', log, name='log'),
    path('logoutUser/', logoutUser, name='logoutUser'),
	path('update_task/<str:pk>/', updateTask, name="update_task"),
	path('delete/<str:pk>/', deleteTask, name="delete"),
]