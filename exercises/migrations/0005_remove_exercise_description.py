# Generated by Django 3.1.6 on 2021-02-27 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0004_auto_20210226_1933"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exercise",
            name="description",
        ),
    ]
