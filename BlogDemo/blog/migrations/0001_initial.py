# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-26 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='文章标题')),
                ('body', models.TextField(verbose_name='文章正文')),
                ('created_time', models.DateTimeField(verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(verbose_name='修改时间')),
                ('excerpt', models.CharField(blank=True, max_length=100, verbose_name='文章摘要')),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
        ),
    ]