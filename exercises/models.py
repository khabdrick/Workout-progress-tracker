from django.db import models

from users.models import User


class Exercise(models.Model):
    # Attributes
    name = models.CharField(null=False, blank=False, max_length=100)
    tips = models.TextField(null=False, blank=True, max_length=1000)
    muscle = models.ManyToManyField("body.Muscle", related_name="muscle")

    # Methods
    def __str__(self):
        return str(self.muscle.all().first()) + " - " + self.name


class ExerciseSet(models.Model):
    # Attributes
    exercise = models.ForeignKey(
        Exercise, null=False, blank=False, on_delete=models.CASCADE
    )
    sets = models.ManyToManyField("exercises.Set", related_name="sets")
    number_of_sets = models.IntegerField(null=False, blank=False, default=3)

    # Methods
    def __str__(self):
        return str(self.exercise.name) + " - " + str(self.number_of_sets) + " sets"


class Set(models.Model):
    # Constants
    REPS_UNIT = (("RE", "Reps"),)
    WEIGHT_UNIT = (("KG", "Kg."), ("BW", "Body Weight"))
    # Attributes
    reps = models.PositiveIntegerField(null=False, blank=False, default=0)
    reps_unit = models.CharField(max_length=2, choices=REPS_UNIT, default="RE")
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    weight_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT, default="RE")

    # Methods
    def __str__(self):
        return (
            str(self.reps)
            + " "
            + str(self.reps_unit)
            + " x "
            + str(self.weight)
            + " "
            + str(self.weight_unit)
        )
