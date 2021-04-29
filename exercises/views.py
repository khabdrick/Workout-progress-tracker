from django.views.generic import FormView
from .models import Exercise
from .forms import ExerciseForm
from django.urls import reverse_lazy


class ExerciseCreateView(FormView):
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"
    success_url = reverse_lazy('logs:log_list')
