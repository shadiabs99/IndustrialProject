# Generated by Django 4.2 on 2023-05-06 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Idea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("idea_title", models.CharField(max_length=50)),
                ("idea_url", models.URLField()),
                ("campaign_id", models.IntegerField(null=True)),
                ("team", models.CharField(max_length=50)),
                ("background", models.TextField(max_length=250)),
                ("solution", models.TextField(max_length=250)),
                ("impact", models.TextField(max_length=250)),
                ("file", models.FileField(blank=True, null=True, upload_to="files/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="idea_create",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="author",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        default=None,
                        related_name="idea_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="idea_update",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="last updated by",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IdeaLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        choices=[("Like", "Like"), ("Unlike", "Unlike")],
                        default="Like",
                        max_length=10,
                    ),
                ),
                (
                    "idea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ideas.idea"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
