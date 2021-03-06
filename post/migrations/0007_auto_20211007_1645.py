# Generated by Django 3.2.8 on 2021-10-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorys',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='categorys',
            name='updated',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='post', to='post.Categorys'),
        ),
    ]
