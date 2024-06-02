# Generated by Django 5.0.2 on 2024-05-18 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapi", "0003_jobfeedback"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobfeedback",
            name="job",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="feedbacks",
                to="webapi.jobs",
            ),
        ),
    ]
