
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



class Program(models.Model):
    # Constants
    TYPE = (('BU', 'Bulking'), ('CU', 'Cutting'), ('MA', 'Maintaining'),)

    # Attributes
    name = models.CharField(null = False, blank = False, max_length = 100)
    summary = models.TextField(null = False, blank = True, max_length = 1500)
    goal = models.CharField(max_length = 2, choices = TYPE, default = 'MA')
    day = models.CharField(max_length=225, choices=DAYS_OF_THE_WEEK)


	# # Methods
	# def __str__(self):
	# 	return self.number + ' ' + self.workout.name
