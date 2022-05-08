from django.urls import path, include
from .views import (
    ExerciseViewSet,
    ExerciseSetViewSet,
    ExerciseCreateAPIView, ExerciseUpdateAPIView
)
from rest_framework import routers

app_name = "exercises"
router = routers.DefaultRouter()
router.register(r"exercises", ExerciseViewSet)  # route for exercises list
router.register(r"exerciseset", ExerciseSetViewSet)  # route for exercise sets list


urlpatterns = [
    path("", include(router.urls)),
    path('create/', ExerciseCreateAPIView.as_view(), name='create_exercise'),
    path('<int:pk>/update/',
         ExerciseUpdateAPIView.as_view(),
         name='update_exercise'),
]
