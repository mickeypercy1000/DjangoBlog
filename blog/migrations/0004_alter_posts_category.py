# Generated by Django 4.0.2 on 2022-02-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_posts_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]