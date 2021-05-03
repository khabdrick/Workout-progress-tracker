from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import WorkoutDayForm, WorkoutSessionForm
from .models import WorkoutDay, WorkoutSession


class WorkoutDayCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutDay
    form_class = WorkoutDayForm
    template_name = "programs/program.html"
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkoutSessionCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    form_class = WorkoutSessionForm
    template_name = "programs/workoutsessionform.html"
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
