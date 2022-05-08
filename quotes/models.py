from django.db import models

class BodyBuilderQuote(models.Model):
    name = models.CharField(max_length=200)
    quote = models.CharField(max_length=1000)

    # Methods
    def __str__(self):
        return self.name

class FitnessDidYouKnowQuote(models.Model):
    quote = models.CharField(max_length=1000)

    # Methods
    def __str__(self):
        return self.quote
