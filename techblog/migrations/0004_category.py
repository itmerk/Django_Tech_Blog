# Generated by Django 5.0.7 on 2024-08-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0003_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]