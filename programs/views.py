from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from .forms import WorkoutDayForm, WorkoutSessionForm
from .models import WorkoutDay, WorkoutSession


class WorkoutDayCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutDay
    form_class = WorkoutDayForm
    template_name = "programs/programform.html"
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


class ProgramView(ListView):
    """Display program"""

    model = WorkoutDay
    template_name = "programs/program.html"
    context_object_name = "program"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return WorkoutDay.objects.filter(user=user).order_by("day_of_week")
