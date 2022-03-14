# Generated by Django 3.2 on 2022-02-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('excerpt', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Draft', 'draft'), ('Published', 'published')], max_length=20)),
                ('category', models.CharField(choices=[('News', 'news'), ('Business', 'business'), ('Health', 'health'), ('Tech', 'tech'), ('Law', 'law')], max_length=20)),
            ],
        ),
    ]
