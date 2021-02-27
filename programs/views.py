from django.shortcuts import render
from .models import Program, ExerciseSet
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
