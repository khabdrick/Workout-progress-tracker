from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import WorkoutLogForm
from .models import WorkoutLog

class WorkoutLogCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutLog
    form_class = WorkoutLogForm
    template_name = "logs/workoutlogform.html"
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
