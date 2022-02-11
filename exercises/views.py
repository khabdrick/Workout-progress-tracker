from django.views.generic import CreateView
from .models import Exercise, Set
from .forms import ExerciseForm, SetForm
from django.urls import reverse_lazy, reverse
from rest_framework import viewsets
from .serializers import ExerciseSerializer


class ExerciseCreateView(CreateView):
    """View to create each Exercise"""

    model = Exercise
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("logs:log_list", args=[self.request.user.username])


class SetCreateView(CreateView):
    """View to create each set for the exercises"""

    model = Set
    form_class = SetForm
    template_name = "exercises/set_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("logs:log_create")


######################################################
class ExerciseViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Exercises.
    """

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
