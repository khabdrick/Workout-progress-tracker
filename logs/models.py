from django.db import models


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

    # Attributes
    day = models.CharField(max_length=225, choices=DAYS_OF_THE_WEEK)

    summary = models.TextField(null=False, blank=True, max_length=1500)
    goal = models.CharField(max_length=2, choices=TYPE, default="MA")
    date = models.DateField(max_length=223, auto_now_add=True)
    exercises = models.ManyToManyField("exercises.ExerciseSet")
    muscles = models.ManyToManyField("body.Muscle")
