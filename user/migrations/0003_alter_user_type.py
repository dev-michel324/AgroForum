# Generated by Django 3.2.7 on 2021-09-29 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('specialist', 'specialist'), ('beginner', 'beginner')], max_length=10),
        ),
    ]
