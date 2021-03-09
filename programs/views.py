from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import WorkoutDayForm, WorkoutSessionForm
from .models import WorkoutDay, WorkoutSession

# class UserGroceryListView(ListView):
#     model = WorkoutDay
#     template_name = 'groceries/user_grocery_list.html'
#     context_object_name = 'workoutday'

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Grocery.objects.filter(user=user).order_by('-date')


class WorkoutDayCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutDay
    form_class = WorkoutDayForm
    template_name = "programs/workoutday.html"
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkoutSessionCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    form_class = WorkoutSessionForm
    template_name = "programs/workoutsession.html"
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
