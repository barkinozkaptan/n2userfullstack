# Generated by Django 5.1.5 on 2025-01-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_comment_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
