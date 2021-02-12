from django.db import models
from django.db.models.base import Model
from users.models import User

DAYS_OF_THE_WEEK = (
    ("monday", "Monday"),
    ("tuesday", "Tuesday"),
    ("wednesday", "Wednesday"),
    ("thursday", "Thursday"),
    ("friday", "Friday"),
    ("saturday", "Saturday"),
    ("sunday", "Sunday"),
    
)

class Exercise(models.Model):
    names=models.CharField(max_length=225)
    reps_goals=models.PositiveIntegerField(max_length=223)
    sets_goals= models.PositiveIntegerField(max_length=223)
    max_weight=models.PositiveIntegerField(max_length=22)



class Day(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=225, choices=DAYS_OF_THE_WEEK)
    excercises = models.ForeignKey(Exercise,related_name="exercise", on_delete=models.CASCADE)
    body_parts = models.CharField(max_length=225)

class WorkoutDailyLog:
    current_date= models.DateField(
        max_length=255,
        null=True,
        blank=True,
        auto_now_add=True
    )
    exercise_reps= models.ForeignKey(WorkorkRegimen,)


