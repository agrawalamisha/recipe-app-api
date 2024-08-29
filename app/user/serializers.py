"""
Serializers for the user API view
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


# ModelSerializer : takes input json and serializes it as per model
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # overriding create() method here to use our custom create_user method
    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
