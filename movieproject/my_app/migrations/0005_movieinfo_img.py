# Generated by Django 5.0.6 on 2024-07-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_movieinfo_delete_movieinfoms'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]