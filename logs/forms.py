from django import forms

from .models import WorkoutLog


class WorkoutLogForm(forms.ModelForm):
    class Meta:
        fields = [
            "day",
            "summary",
            "goal",
            "exercises",
            "muscles",
        ]
        model = WorkoutLog
        widgets = {
            "day": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "goal": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "exercises": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "muscles": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }
