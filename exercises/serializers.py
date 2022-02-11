from attr import fields
from rest_framework import serializers
from .models import Exercise, ExerciseSet, Set

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Exercise
        fields = ('name', 'tips')
