from django.db import models
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField

DAYS_OF_THE_WEEK = (
    ("monday", "Monday"),
    ("tuesday", "Tuesday"),
    ("wednesday", "Wednesday"),
    ("thursday", "Thursday"),
    ("friday", "Friday"),
    ("saturday", "Saturday"),
    ("sunday", "Sunday"),
)



class WorkoutLog(models.Model):
    TYPE = (
        ("BU", "Bulking"),
        ("CU", "Cutting"),
        ("MA", "Maintaining"),
    )
    MUSCLE_GROUP = (
        ("Calves", "Calves"),
        ("Hamstrings", "Hamstrings"),
        ("quads", "Quadriceps(quads)"),
        ("glutes", "Glutes"),
        ("biceps", "Biceps"),
        ("triceps", "Triceps"),
        ("forearms", "Forearms"),
        ("traps", "Trapezius(traps)"),
    )

    # Attributes
    day = models.CharField(max_length=225, choices=DAYS_OF_THE_WEEK)
    summary = models.TextField(null=False, blank=True, max_length=1500)
    goal = models.CharField(max_length=2, choices=TYPE, default="MA")
    date = models.DateField(max_length=223, auto_now_add=True)
    exercises = models.ManyToManyField(to="exercises.ExerciseSet", blank=True,)
    muscles = MultiSelectField(max_length=100, choices=MUSCLE_GROUP, default=None)

    # Methods
    def __str__(self):
        return self.day