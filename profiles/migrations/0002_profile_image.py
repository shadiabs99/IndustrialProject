# Generated by Django 4.2 on 2023-06-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/profile_pics/"
            ),
        ),
    ]
