from datetime import datetime, timedelta

# Django imports
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


class WorkoutDay(models.Model):
    # Constants
    DAY = (
        ("MO", "Monday"),
        ("TU", "Tuesday"),
        ("WE", "Wednesday"),
        ("TH", "Thursday"),
        ("FR", "Friday"),
        ("SA", "Saturday"),
        ("SU", "Sunday"),
    )

    # Attributes
    day_of_week = models.CharField(max_length=2, choices=DAY, default="MO")
    session = models.ForeignKey(
        "programs.WorkoutSession", null=False, on_delete=models.CASCADE
    )

    # Methods
    def __str__(self):
        return self.day_of_week + " - " + self.session.name


class WorkoutSession(models.Model):
    # Attributes
    name = models.CharField(null=False, blank=False, max_length=100)
    summary = models.TextField(null=False, blank=True, max_length=1000)
    exercises = models.ManyToManyField("exercises.ExerciseSet")

    # Methods
    def __str__(self):
        return self.name
