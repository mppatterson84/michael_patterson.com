from django.contrib.auth import get_user_model
from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # due_by = serializers.DateTimeField(format="%A, %B %d, %Y, %I:%M %p")

    class Meta:
        model = Todo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)