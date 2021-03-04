from django import forms
from django.forms import widgets

from .models import WorkoutDay, WorkoutSession

class WorkoutDayForm(forms.ModelForm):
    class Meta:
        fields = ["day_of_week", "session",]
        model = WorkoutDay
        widgets={
            'day_of_week': forms.Select(
                attrs={'class':'form-control',}
            ),
            'session': forms.Select(
                attrs={'class':'form-control',}
            )
        }
          

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        fields = ["name", "summary", "exercises"]
        model = WorkoutSession
        widgets={
            'name': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Name'}
            ),
            'summary': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Summary'}
            ),
            'exercises': forms.Select(
                attrs={'class':'form-control',}
            )
        }
                    