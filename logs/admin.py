from django.contrib import admin
from .forms import WorkoutLogForm
from .models import WorkoutLog


# class LogAdmin(admin.ModelAdmin):
#     form = WorkoutLogForm


admin.site.register(WorkoutLog)
