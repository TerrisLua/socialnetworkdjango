# Generated by Django 3.2.20 on 2023-08-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MTapp", "0015_alter_appuser_media"),
    ]

    operations = [
        migrations.AddField(
            model_name="appuser",
            name="text_content",
            field=models.TextField(blank=True, null=True),
        ),
    ]
