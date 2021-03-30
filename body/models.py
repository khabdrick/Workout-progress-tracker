from django.db import models


class MuscleGroup(models.Model):
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
    # Attributes
    name = models.CharField(
        null=False, blank=False, max_length=100, choices=MUSCLE_GROUP
    )

    # Methods
    def __str__(self):
        return self.name
