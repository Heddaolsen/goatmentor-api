from rest_framework import viewsets

from training import models
from training import serializers


class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = models.Training_sessions.objects.all()
    serializer_class = serializers.TrainingSessionSerializer
