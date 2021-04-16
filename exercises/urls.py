from django.urls import path
from .views import ExerciseCreateView

app_name = "exercises"

urlpatterns = [
    path("exercise_form/", ExerciseCreateView.as_view(), name="exercise_create"),
]
