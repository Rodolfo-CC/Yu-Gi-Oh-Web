# Generated by Django 5.2.1 on 2025-05-18 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cards/'),
        ),
    ]
