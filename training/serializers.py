from rest_framework import serializers

from .models import Training_sessions

class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training_sessions
        fields = ['id', 'user', 'drill', 'minutes']
