# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscanners', '0008_delete_status_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='burp_issue_definitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type_id', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
