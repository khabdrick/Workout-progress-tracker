from .models import Exercise, Set, ExerciseSet
from rest_framework import viewsets
from .serializers import ExerciseSerializer, ExerciseSetSerializer
from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from exercises.permissions import IsOwner


class ExerciseCreateAPIView(CreateAPIView):
    """
    Create new Exercise.\n

    Requires authentication. Returns exercise details.\n
    Request body format:\n
        {\n
            "name": "string",\n
            "tips": "string",\n
        }\n
    """

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class ExerciseUpdateAPIView(UpdateAPIView):
    """
    Update exercise.

    Requires authentication.\n
    Requires exercise id.\n
    Returns exercise details.\n
    request body format:\n
        {\n
            "name": "string",\n
            "tips": "string",\n
        }\n
    """

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    # def perform_update(self, serializer):
    #     try:
    #         old = Exercise.objects.get(pk=self.kwargs.get("pk"))
    #     except Exercise.DoesNotExist:
    #         pass

    #     new = serializer.save(creator=self.request.user)
    #     self.request.user.save()

    #     if project_changed(old, new):
    #         info = {
    #             "exercise_id": str(new.pk),
    #             "editor": self.request.user.username
    #         }
    #         activity_notification(["edited_project"], **info)

    #     # because project_changed still needs to make reference to the
    #     # old publishing rule, it wasn't deleted in the serializer update method,
    #     # instead we delete it here after project_changed has done it's part.
    #     old.publish.delete()


# class ProjectDeleteAPIView(DestroyAPIView):
#     """
#     Delete a project from database.

#     Requires authentication.
#     Requires project id.
#     Returns {details: "ok"}
#     """
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated, IsOwner]
#     throttle_classes = [CustomUserRateThrottle, SustainedRateThrottle]

#     def delete(self, request, *args, **kwargs):
#         project = self.get_object()
#         if project:
#             result = self.destroy(request, *args, **kwargs)
#             request.user.save()
#             return result


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Exercises.
    """

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseSetViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Exercise sets.
    """

    queryset = ExerciseSet.objects.all()
    serializer_class = ExerciseSetSerializer
