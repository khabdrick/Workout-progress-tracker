# Generated by Django 3.1.6 on 2021-02-27 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_delete_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutsession',
            name='recommendations',
        ),
    ]
