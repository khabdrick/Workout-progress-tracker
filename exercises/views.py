from django.views.generic import FormView
from .models import Exercise
from .forms import ExerciseForm

class ExerciseCreateView(FormView):
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"
