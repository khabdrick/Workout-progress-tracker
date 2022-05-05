# Generated by Django 3.1.7 on 2021-05-10 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("programs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workoutday",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userprogram",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
