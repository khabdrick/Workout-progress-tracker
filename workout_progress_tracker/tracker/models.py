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
    excercises1 = models.ForeignKey(Exercise,related_name="exercises1", on_delete=models.CASCADE)
    excercises2 = models.ForeignKey(Exercise,related_name="exercises2", on_delete=models.CASCADE)
    excercises3 = models.ForeignKey(Exercise,related_name="exercises3", on_delete=models.CASCADE)
    excercises4 = models.ForeignKey(Exercise,related_name="exercises4", on_delete=models.CASCADE)
    excercises5 = models.ForeignKey(Exercise,related_name="exercises5", on_delete=models.CASCADE)
    excercises6 = models.ForeignKey(Exercise,related_name="exercises6", on_delete=models.CASCADE)
    excercises7 = models.ForeignKey(Exercise,related_name="exercises7", on_delete=models.CASCADE)
    excercises8 = models.ForeignKey(Exercise,related_name="exercises8", on_delete=models.CASCADE)
    excercises9 = models.ForeignKey(Exercise,related_name="exercises9", on_delete=models.CASCADE)
    excercises10 = models.ForeignKey(Exercise,related_name="exercises10", on_delete=models.CASCADE)


    body_parts = models.CharField(max_length=225)

class WorkoutDailyLog(models.Model):
    day_of_the_week = models.CharField(max_length=225, choices=DAYS_OF_THE_WEEK)
    current_date= models.DateTimeField(
        max_length=255,
        null=True,
        blank=True,
        auto_now_add=True
    )

    exercise_reps= models.ForeignKey()


