"""
Views for the user API.
"""

from rest_framework import generics

from user.serializers import UserSerializer

# generics.CreateAPIView : Handles POST request for creating DB objects
# whose serializer class has been defined
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
