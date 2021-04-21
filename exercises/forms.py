from django import forms
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        fields = [
            "name",
            "tips",
            # "muscle",
        ]
        model = Exercise
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "tips": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows":"3"
                }
            ),
            # "muscle": forms.CheckboxSelectMultiple(
            #     attrs={"class": "list-unstyled", "type": "checkbox"}
            # ),
        }
