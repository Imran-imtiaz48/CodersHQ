# Generated by Django 3.0.11 on 2021-02-15 13:22

import codershq.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_github_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=codershq.users.models.user_image_path, verbose_name='Profile image'),
        ),
    ]
