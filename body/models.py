from django.db import models


class MuscleGroup(models.Model):
    # Attributes
    name = models.CharField(null=False, blank=False, max_length=100)

    # Methods
    def __str__(self):
        return self.name
