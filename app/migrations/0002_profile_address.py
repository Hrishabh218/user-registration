# Generated by Django 5.0 on 2024-01-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
