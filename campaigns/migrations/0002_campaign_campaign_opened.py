# Generated by Django 4.2 on 2023-06-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="campaign_opened",
            field=models.BooleanField(default=True),
        ),
    ]