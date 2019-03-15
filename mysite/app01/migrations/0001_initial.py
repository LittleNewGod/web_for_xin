# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-19 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asin_detail', models.CharField(max_length=32)),
                ('Total_reviews_detail', models.CharField(max_length=32)),
                ('Total_score_detail', models.CharField(max_length=32)),
                ('Asin_tag', models.CharField(max_length=32)),
                ('Reviewer', models.CharField(max_length=32)),
                ('Stars', models.CharField(max_length=32)),
                ('Title', models.CharField(max_length=32)),
                ('Date', models.CharField(max_length=32)),
                ('Review', models.CharField(max_length=32)),
                ('Tag', models.CharField(max_length=32)),
                ('Review_content', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asin', models.CharField(max_length=32)),
                ('Total_reviews', models.CharField(max_length=32)),
                ('Total_score', models.CharField(max_length=32)),
            ],
        ),
    ]
