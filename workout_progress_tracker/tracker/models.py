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

class WorkourkRegimen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day= models.CharField(max_length=225, )
    excercise= models.ForeignKey(Exercise, on_delete=models.CASCADE)




