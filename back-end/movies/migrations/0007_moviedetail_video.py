# Generated by Django 3.2.18 on 2023-05-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_moviedetail_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetail',
            name='video',
            field=models.TextField(null=True),
        ),
    ]