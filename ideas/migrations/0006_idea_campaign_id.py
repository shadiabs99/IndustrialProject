# Generated by Django 4.1.4 on 2023-01-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ideas", "0005_remove_idea_campaign_ptr_idea_author_idea_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="idea",
            name="campaign_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
