# Generated by Django 3.1.7 on 2021-03-25 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("body", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("tips", models.TextField(blank=True, max_length=1000)),
                (
                    "muscle",
                    models.ManyToManyField(
                        related_name="muscle", to="body.MuscleGroup"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Set",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reps", models.PositiveIntegerField(default=0)),
                (
                    "reps_unit",
                    models.CharField(
                        choices=[("RE", "Reps")], default="RE", max_length=2
                    ),
                ),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "weight_unit",
                    models.CharField(
                        choices=[("KG", "Kg."), ("BW", "Body Weight")],
                        default="RE",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExerciseSet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_sets", models.IntegerField(default=3)),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exercises.exercise",
                    ),
                ),
                (
                    "sets",
                    models.ManyToManyField(related_name="sets", to="exercises.Set"),
                ),
            ],
        ),
    ]
