# Generated by Django 4.0.2 on 2022-03-15 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_categories_created_at_categories_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_summary',
            field=models.TextField(max_length=100, null=True),
        ),
    ]