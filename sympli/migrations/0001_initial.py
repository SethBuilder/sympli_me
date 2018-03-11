# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 12:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10000)),
                ('description', models.CharField(blank=True, max_length=50000)),
                ('article_link', models.URLField()),
                ('thumbnail_link', models.URLField(blank=True, max_length=5000)),
                ('thumbnail_desc', models.CharField(blank=True, max_length=15000)),
                ('thumbnail_image', models.ImageField(blank=True, max_length=5000, upload_to='article_thumbnails')),
                ('thumbnail_desc_slug', models.SlugField(allow_unicode=True, default='test-slug-ar', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('frequency', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('logo_image', models.ImageField(blank=True, upload_to='logo_images')),
                ('logo_link', models.URLField(blank=True)),
                ('logo_title', models.CharField(blank=True, max_length=1000)),
                ('logo_title_slug', models.SlugField()),
                ('link', models.URLField(blank=True)),
                ('last_updated', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('frequency', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('prof_pic', models.ImageField(blank=True, upload_to='prof_pictures')),
                ('interests', models.ManyToManyField(blank=True, to='sympli.Interest')),
                ('liked_articles', models.ManyToManyField(default=0, to='sympli.Like')),
                ('magazines', models.ManyToManyField(blank=True, to='sympli.Magazine')),
            ],
        ),
        migrations.AddField(
            model_name='magazine',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='magazine',
            name='content',
            field=models.ManyToManyField(blank=True, to='sympli.Article'),
        ),
        migrations.AddField(
            model_name='like',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='liked_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sympli.Article'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sympli.ContentSource'),
        ),
    ]