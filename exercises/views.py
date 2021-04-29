from django.views.generic import CreateView
from .models import Exercise
from .forms import ExerciseForm
from django.urls import reverse
from django.http import HttpResponseRedirect



class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("logs:log_list", args=[request.user.username]))
        return super().get(request, *args, **kwargs)



