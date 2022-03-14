# Generated by Django 4.0.2 on 2022-03-14 19:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_categories_alter_posts_options_remove_posts_excerpt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
