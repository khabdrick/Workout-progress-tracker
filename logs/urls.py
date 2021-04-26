from django.urls import path
from .views import WorkoutLogCreateView, WorkoutLogListView

app_name = "logs"

urlpatterns = [
    path("log_form/", WorkoutLogCreateView.as_view(), name="log_create"),
    path("log_list/", WorkoutLogListView.as_view(), name="log_list"),
]
