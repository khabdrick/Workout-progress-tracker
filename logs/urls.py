from django.urls import path

from .views import WorkoutLogCreateView

app_name = "programs"

urlpatterns = [
    path("log_form/", WorkoutLogCreateView.as_view(), name="log_create"),
]
