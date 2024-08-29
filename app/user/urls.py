"""
URL mappings for the User API
"""
from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    # name create used for reverse lookup
    path('create/', views.CreateUserView.as_view(), name='create'),
]
