from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
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

class UserGroceryListView(ListView):
    model = WorkoutLog
    template_name = 'logs/workoutloglist.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'grocery'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Grocery.objects.filter(user=user).order_by('-date')

