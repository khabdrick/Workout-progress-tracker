# Generated by Django 3.1.7 on 2021-03-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musclegroup',
            name='name',
            field=models.CharField(choices=[('calves', 'Calves'), ('hamstrings', 'Hamstrings'), ('quads', 'Quadriceps(quads)'), ('glutes', 'Glutes'), ('biceps', 'Biceps'), ('triceps', 'Triceps'), ('forearms', 'Forearms'), ('traps', 'Trapezius(traps)')], max_length=100),
        ),
    ]
