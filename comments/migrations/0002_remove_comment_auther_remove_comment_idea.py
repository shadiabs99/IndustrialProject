# Generated by Django 4.1.4 on 2023-01-20 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="auther",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="idea",
        ),
    ]