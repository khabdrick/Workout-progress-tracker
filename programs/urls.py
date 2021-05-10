from django.urls import path

from .views import WorkoutDayCreateView, WorkoutSessionCreateView, ProgramView

app_name = "programs"

urlpatterns = [
    path("day/", WorkoutDayCreateView.as_view(), name="day"),
    path("program/<str:username>/", ProgramView.as_view(), name="program"),
    path("session/", WorkoutSessionCreateView.as_view(), name="session"),
]
