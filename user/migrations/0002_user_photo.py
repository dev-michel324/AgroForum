# Generated by Django 3.2.7 on 2021-09-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static/profile_photos'),
        ),
    ]
