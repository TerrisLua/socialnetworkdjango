# Generated by Django 3.2.20 on 2023-08-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MTapp", "0009_alter_appuser_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="image",
            field=models.FileField(default="defaultdp.jpg", upload_to=""),
        ),
    ]
