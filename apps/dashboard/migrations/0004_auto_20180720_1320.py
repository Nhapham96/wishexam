# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-20 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('dashboard', '0003_auto_20180720_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('add_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add', to='login.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='list',
            name='added_by',
        ),
        migrations.AddField(
            model_name='list',
            name='added_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='added', to='login.User'),
            preserve_default=False,
        ),
    ]