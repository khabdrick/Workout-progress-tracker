from django import forms
from .models import Exercise, Set


class ExerciseForm(forms.ModelForm):
    class Meta:
        fields = ["name", "tips"]
        model = Exercise
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "tips": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
        }


class SetForm(forms.ModelForm):
    class Meta:
        fields = ["reps", "reps_unit", "weight", "weight_unit"]
        model = Set
        widgets = {
            "reps": forms.NumberInput(attrs={"class": "form-control"}),
            "reps_unit": forms.CheckboxSelectMultiple(
                attrs={"class": "list-unstyled", "type": "checkbox"}
            ),
            "weight": forms.NumberInput(attrs={"class": "form-control", "rows": "3"}),
            "weight_unit": forms.CheckboxSelectMultiple(
                attrs={"class": "list-unstyled", "type": "checkbox"}
            ),
        }
