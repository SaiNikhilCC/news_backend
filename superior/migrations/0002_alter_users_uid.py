# Generated by Django 4.1.7 on 2023-03-09 05:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("superior", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("8fc11df2-a601-4bc0-8c36-478417b78b24"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
