# Generated by Django 4.0.2 on 2022-02-27 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_posts_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='created_at',
        ),
    ]