# Generated by Django 4.1.4 on 2023-01-20 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='campaigns',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='user',
        ),
    ]
