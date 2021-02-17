from django.db import models


class RegimenExercise(models.Model):
    names = models.CharField(max_length=225)
    reps_goals = models.PositiveIntegerField(max_length=223)
    sets_goals = models.PositiveIntegerField(max_length=223)
    max_weight = models.PositiveIntegerField(max_length=22)


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


class Day(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=225, choices=DAYS_OF_THE_WEEK)
    excercises1 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises1", on_delete=models.CASCADE
    )
    excercises2 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises2", on_delete=models.CASCADE
    )
    excercises3 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises3", on_delete=models.CASCADE
    )
    excercises4 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises4", on_delete=models.CASCADE
    )
    excercises5 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises5", on_delete=models.CASCADE
    )
    excercises6 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises6", on_delete=models.CASCADE
    )
    excercises7 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises7", on_delete=models.CASCADE
    )
    excercises8 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises8", on_delete=models.CASCADE
    )
    excercises9 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises9", on_delete=models.CASCADE
    )
    excercises10 = models.ForeignKey(
        RegimenExercise, related_name="RegimenExercises10", on_delete=models.CASCADE
    )

    body_parts = models.CharField(max_length=225)
