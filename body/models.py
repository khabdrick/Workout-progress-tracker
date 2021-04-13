from django.db import models

MUSCLE_GROUP = (
    ("calves", "Calves"),
    ("hamstrings", "Hamstrings"),
    ("quads", "Quadriceps(quads)"),
    ("glutes", "Glutes"),
    ("biceps", "Biceps"),
    ("triceps", "Triceps"),
    ("forearms", "Forearms"),
    ("traps", "Trapezius(traps)"),
)


class MuscleGroup(models.Model):
    # Attributes
    name = models.CharField(max_length=100, choices=MUSCLE_GROUP, default=None)

    # Methods
    def __str__(self):
        return self.name
