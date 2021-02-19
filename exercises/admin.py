from django.contrib import admin

from .models import Exercise, ExerciseSet, Set

admin.site.register(Exercise)
admin.site.register(ExerciseSet)
admin.site.register(Set)

