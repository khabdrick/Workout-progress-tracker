from django.db import models

class RegimenExercise(models.Model):
    names=models.CharField(max_length=225)
    reps_goals=models.PositiveIntegerField(max_length=223)
    sets_goals= models.PositiveIntegerField(max_length=223)
    max_weight=models.PositiveIntegerField(max_length=22)

