from django.urls import path
from . import views

urlpatterns = [
    path('graphql/', views.hidden_api_info, name='hidden_api_info'),

    # Add more API endpoints here
]