from training.viewsets import TrainingSessionViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('training-sessions', TrainingSessionViewSet)