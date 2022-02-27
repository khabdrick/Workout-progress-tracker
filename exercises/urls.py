from django.urls import path, include
from .views import ExerciseCreateView, SetCreateView, ExerciseViewSet, ExerciseSetViewSet
from rest_framework import routers

app_name = "exercises"
router = routers.DefaultRouter()
router.register(r"exercises", ExerciseViewSet)  # route for exercises
router.register(r"exerciseset", ExerciseSetViewSet)  # route for exercise sets


urlpatterns = [
    path("", include(router.urls)),
    path("exercise_form/", ExerciseCreateView.as_view(), name="exercise_create"),
    path("set_form/", SetCreateView.as_view(), name="set_create"),
]
