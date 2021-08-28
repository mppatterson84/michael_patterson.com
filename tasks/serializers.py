from django.contrib.auth import get_user_model
from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    due_by = serializers.DateTimeField(format="%A, %B %d, %Y, %I:%M %p")

    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)