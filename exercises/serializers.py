from attr import fields
from rest_framework import serializers
from .models import Exercise, ExerciseSet, Set


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ("name", "tips")

class ExerciseSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseSet

    def to_representation(self, instance):
        representation = dict()
        representation["exercise"] = instance.exercise.name
        representation["exercise"] = instance.exercise.tips
        representation["sets"] = instance.exercises.Set
        representation["number_of_sets"] = instance.number_of_sets
