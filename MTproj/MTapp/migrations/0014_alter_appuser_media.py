# Generated by Django 3.2.20 on 2023-08-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MTapp", "0013_appuser_media"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="media",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
