# Generated by Django 4.1.4 on 2023-01-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0002_alter_campaign_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="image",
            field=models.ImageField(
                upload_to="images/<django.db.models.fields.CharField>/"
            ),
        ),
    ]
