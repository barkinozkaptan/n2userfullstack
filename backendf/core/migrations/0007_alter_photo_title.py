# Generated by Django 5.1.5 on 2025-01-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_album_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
