
from .views import *
from django.urls import path

urlpatterns = [
    path('', challenge_list, name='challenge_list'),
    path('challenge/<int:pk>/', challenge_detail, name='challenge_detail'), 
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
]
