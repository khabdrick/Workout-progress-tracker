from django.contrib import admin
from .models import Program, WorkoutDay, WorkoutSession

admin.site.register(Program)
admin.site.register(WorkoutDay)
admin.site.register(WorkoutSession)
