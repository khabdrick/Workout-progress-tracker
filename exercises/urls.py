from django.urls import path
from .views import ExerciseCreateView, SetCreateView

app_name = "exercises"

urlpatterns = [
    path("exercise_form/", ExerciseCreateView.as_view(), name="exercise_create"),
    path("set_form/", SetCreateView.as_view(), name="set_create"),
    
]
