# Generated by Django 4.0.2 on 2022-03-15 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_categories_category_img_posts_post_img1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post_img1',
            new_name='post_img',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='post_img2',
        ),
    ]
