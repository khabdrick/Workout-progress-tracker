from django.views.generic import CreateView
from .models import Exercise
from .forms import ExerciseForm
from django.urls import reverse_lazy


class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"
    success_url = reverse_lazy('logs:log_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)