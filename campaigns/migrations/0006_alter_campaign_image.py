# Generated by Django 4.1.4 on 2023-01-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_campaign_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]