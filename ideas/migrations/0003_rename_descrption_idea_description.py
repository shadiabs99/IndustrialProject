# Generated by Django 4.1.4 on 2023-01-17 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ideas", "0002_idea_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="idea",
            old_name="descrption",
            new_name="description",
        ),
    ]