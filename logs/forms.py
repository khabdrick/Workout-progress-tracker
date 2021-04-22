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
            "summary": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "goal": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "exercises": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "list-unstyled",
                }
            ),
            "muscles": forms.CheckboxSelectMultiple(
                attrs={"class": "list-unstyled", "type": "checkbox"}
            ),
        }
