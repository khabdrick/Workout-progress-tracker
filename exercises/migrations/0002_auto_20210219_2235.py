# Generated by Django 3.1.6 on 2021-02-19 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0001_initial'),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='body_part',
            field=models.ManyToManyField(related_name='body_part', to='body.BodyPart'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='tips',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]