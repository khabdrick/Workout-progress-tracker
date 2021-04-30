from django.views.generic import CreateView
from .models import Exercise
from .forms import ExerciseForm
from django.urls import reverse



class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('logs:log_list', args=[self.request.user.username])

