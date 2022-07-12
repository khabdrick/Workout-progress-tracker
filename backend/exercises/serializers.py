from rest_framework import serializers
from .models import Exercise, ExerciseSet, Set


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ("name", "tips", "id")


class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSet
        fields = "__all__"
        depth = 1
