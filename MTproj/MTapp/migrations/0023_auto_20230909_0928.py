# Generated by Django 3.2.20 on 2023-09-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MTapp', '0022_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='image',
            field=models.ImageField(default='defaultdp.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]