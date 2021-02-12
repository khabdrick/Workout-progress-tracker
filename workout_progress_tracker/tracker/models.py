from django.db import models
from django.db.models.base import Model
from users.models import User

CHOICES = (
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

class WorkorkRegimen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day= models.CharField(max_length=225, choices=CHOICES)
    excercise= models.ForeignKey(Exercise,related_name="exercise", on_delete=models.CASCADE)
    body_part = models.CharField(max_length=225)

class WorkoutDailyLog:
    current_date= models.DateField(
        max_length=255,
        null=True,
        blank=True,
        auto_now_add=True
    )
    exercise_reps= models.ForeignKey(WorkorkRegimen,)


