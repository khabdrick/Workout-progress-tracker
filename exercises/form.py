from django import forms
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        fields = [
            "name",
            "tips",
            "muscle",
        ]
        model = Exercise
