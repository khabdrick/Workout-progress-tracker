# Generated by Django 3.1.6 on 2021-02-18 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True, max_length=1500)),
                ('goal', models.CharField(choices=[('BU', 'Bulking'), ('CU', 'Cutting'), ('MA', 'Maintaining')], default='MA', max_length=2)),
                ('day', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True, max_length=1000)),
                ('recommendations', models.TextField(blank=True, max_length=1000)),
                ('exercises', models.ManyToManyField(to='exercises.ExerciseSet')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], default='MO', max_length=2)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.workoutsession')),
            ],
        ),
    ]