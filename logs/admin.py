from django.contrib import admin
from .models import WorkoutLog


# class LogAdmin(admin.ModelAdmin):
#     form = WorkoutLogForm


admin.site.register(WorkoutLog)
