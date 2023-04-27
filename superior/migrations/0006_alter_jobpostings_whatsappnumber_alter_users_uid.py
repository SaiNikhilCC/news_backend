# Generated by Django 4.1.7 on 2023-03-10 12:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("superior", "0005_epaper_alter_users_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpostings",
            name="whatsappNumber",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("53235499-6332-45f7-bc52-41219aec4acc"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]