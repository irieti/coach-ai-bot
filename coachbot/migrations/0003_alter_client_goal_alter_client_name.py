# Generated by Django 5.1.2 on 2024-12-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coachbot", "0002_rename_repetitions_exercise_reps"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="goal",
            field=models.CharField(
                choices=[
                    ("похудение", "Похудение"),
                    ("набор массы", "Набор массы"),
                    ("тонус", "Тонус"),
                ],
                default="похудение",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
