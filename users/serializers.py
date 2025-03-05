from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'food_restrictions', 'is_active', 'date_joined']
        read_only_fields = ['id', 'is_active', 'date_joined']
