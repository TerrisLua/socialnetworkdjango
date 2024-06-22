# Generated by Django 3.2.20 on 2023-07-16 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PfamDescription",
            fields=[
                (
                    "pfam_id",
                    models.CharField(max_length=256, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="ProteinSequence",
            fields=[
                (
                    "protein_id",
                    models.CharField(max_length=256, primary_key=True, serialize=False),
                ),
                ("sequence", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Dataset",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("organism_id", models.CharField(max_length=255)),
                ("organism_identifier", models.CharField(max_length=255)),
                ("organism_name", models.CharField(max_length=255)),
                ("domain_description", models.CharField(max_length=255)),
                ("domain_start", models.IntegerField()),
                ("domain_end", models.IntegerField()),
                ("protein_length", models.IntegerField()),
                (
                    "domain_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="MTapp.pfamdescription",
                    ),
                ),
                (
                    "protein_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="MTapp.proteinsequence",
                    ),
                ),
            ],
        ),
    ]