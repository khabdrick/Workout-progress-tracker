from django.urls import path

from .views import WorkoutDayCreateView, WorkoutSessionCreateView

app_name = "programs"

urlpatterns = [
    path("day/", WorkoutDayCreateView.as_view(), name="day"),
    path("session/", WorkoutSessionCreateView.as_view(), name="session"),
]
