# Generated by Django 4.1.4 on 2023-01-20 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ideas", "0004_rename_description_idea_idea_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="idea",
            name="campaign_ptr",
        ),
        migrations.AddField(
            model_name="idea",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="idea_create",
                to=settings.AUTH_USER_MODEL,
                verbose_name="author",
            ),
        ),
        migrations.AddField(
            model_name="idea",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="idea",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="idea_update",
                to=settings.AUTH_USER_MODEL,
                verbose_name="last updated by",
            ),
        ),
    ]
