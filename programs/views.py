from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import WorkoutSession, WorkoutDay
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import WorkoutDayForm, WorkoutSessionForm


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# class UserGroceryListView(ListView):
#     model = WorkoutDay
#     template_name = 'groceries/user_grocery_list.html'  
#     context_object_name = 'workoutday'

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Grocery.objects.filter(user=user).order_by('-date')



class GroceryCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutDay
    form_class = WorkoutDayForm
    template_name = 'programs/workoutday.html'
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GroceryCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    form_class = WorkoutSessionForm
    template_name = 'programs/workoutsession.html'
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)