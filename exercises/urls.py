from django.urls import path, include
from .views import (
    ExerciseViewSet,
    ExerciseSetViewSet,
    ExerciseCreateAPIView
)
from rest_framework import routers

app_name = "exercises"
router = routers.DefaultRouter()
router.register(r"exercises", ExerciseViewSet)  # route for exercises
router.register(r"exerciseset", ExerciseSetViewSet)  # route for exercise sets


urlpatterns = [
    path("", include(router.urls)),


]
