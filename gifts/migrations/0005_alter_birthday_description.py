# Generated by Django 5.0.6 on 2024-06-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts", "0004_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="birthday",
            name="description",
            field=models.TextField(),
        ),
    ]