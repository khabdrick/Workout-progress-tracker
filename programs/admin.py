from django.contrib import admin
from .models import  WorkoutDay, WorkoutSession


admin.site.register(WorkoutDay)
admin.site.register(WorkoutSession)
