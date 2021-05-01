from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .forms import WorkoutLogForm
from .models import WorkoutLog
from django.contrib.auth.models import User


class WorkoutLogCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutLog
    form_class = WorkoutLogForm
    template_name = "logs/workoutlogform.html"
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkoutLogListView(ListView):
    """Display Log list"""

    model = WorkoutLog
    template_name = "logs/workoutloglist.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "log"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return WorkoutLog.objects.filter(user=user).order_by("-date")
