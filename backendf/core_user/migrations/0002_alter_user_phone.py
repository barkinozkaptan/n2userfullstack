# Generated by Django 5.1.5 on 2025-02-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
