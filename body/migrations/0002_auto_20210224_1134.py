# Generated by Django 3.1.6 on 2021-02-24 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0002_auto_20210219_2235"),
        ("body", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BodyPart",
            new_name="Muscle",
        ),
    ]
