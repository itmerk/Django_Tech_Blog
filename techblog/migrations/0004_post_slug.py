# Generated by Django 5.0.7 on 2024-08-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='example-slug', unique=True),
            preserve_default=False,
        ),
    ]
