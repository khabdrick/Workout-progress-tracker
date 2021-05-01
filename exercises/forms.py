from django import forms
from .models import Exercise, Set


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
            "tips": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            # "muscle": forms.CheckboxSelectMultiple(
            #     attrs={"class": "list-unstyled", "type": "checkbox"}
            # ),
        }


class SetForm(forms.ModelForm):
    class Meta:
        fields = [
            "reps",
            "reps_unit",
            "weight",
            "weight_unit",
        ]
        model = Set
        widgets = {
            "reps": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "reps_unit": forms.Textarea(
                attrs={
                    "class": "list-unstyled",
                    "type": "checkbox",
                }
            ),
            "weight": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "weight_unit": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "list-unstyled",
                    "type": "checkbox",
                }
            ),

        }
