# Generated by Django 3.2.20 on 2023-08-23 15:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("MTapp", "0018_alter_mediapost_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Dataset",
        ),
        migrations.DeleteModel(
            name="PfamDescription",
        ),
        migrations.DeleteModel(
            name="ProteinSequence",
        ),
    ]
