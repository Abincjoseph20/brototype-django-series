# Generated by Django 5.0.6 on 2024-06-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_movieinfoms_delete_movieinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieinfoms',
            name='titel',
        ),
        migrations.AddField(
            model_name='movieinfoms',
            name='title',
            field=models.CharField(default=2, max_length=60),
            preserve_default=False,
        ),
    ]
