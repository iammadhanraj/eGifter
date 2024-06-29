# Generated by Django 5.0.6 on 2024-06-29 08:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts", "0003_delete_bithday"),
    ]

    operations = [
        migrations.CreateModel(
            name="Birthday",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("age", models.IntegerField()),
                ("creator", models.CharField(max_length=255)),
                ("img", models.ImageField(upload_to="gifts/birthday/images")),
                ("description", models.TextField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Birthday",
                "verbose_name_plural": "Birthdays",
            },
        ),
    ]
