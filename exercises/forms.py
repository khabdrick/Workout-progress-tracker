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
        widgets = {
            "name": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "tips": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "muscle": forms.CheckboxSelectMultiple(
                attrs={"class": "list-unstyled", "type": "checkbox"}
            ),
        }
