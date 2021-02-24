from django.db import models

class Muscle(models.Model):
	# Attributes
	name = models.CharField(null = False, blank = False, max_length = 100)

	# Methods
	def __str__(self):
		return self.name