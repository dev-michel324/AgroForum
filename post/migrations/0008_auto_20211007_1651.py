# Generated by Django 3.2.8 on 2021-10-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20211007_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
