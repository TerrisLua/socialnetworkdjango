# Generated by Django 3.2.20 on 2023-08-22 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("MTapp", "0017_auto_20230822_0749"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mediapost",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="MTapp.appuser"
            ),
        ),
    ]