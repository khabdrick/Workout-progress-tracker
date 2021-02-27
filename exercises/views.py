from django.shortcuts import render
from .models import Exercise, ExerciseSet
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# class ExerciseCreateView:
