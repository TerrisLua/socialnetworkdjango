# Generated by Django 3.2.20 on 2023-08-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MTapp", "0006_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="thumbnail",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
