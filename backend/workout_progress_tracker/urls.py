from django.contrib import admin
from django.urls import include, path
from exercises.views import ExerciseViewSet
from rest_framework import routers


urlpatterns = [
    path("super/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("exercises/", include("exercises.urls", namespace="exercises")),
    path("programs/", include("programs.urls", namespace="programs")),
    path("logs/", include("logs.urls", namespace="logs")),
]
