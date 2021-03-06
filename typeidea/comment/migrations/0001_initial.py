# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-10 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name='\u5185\u5bb9')),
                ('nickname', models.CharField(max_length=50, verbose_name='\u6635\u79f0')),
                ('website', models.URLField(verbose_name='\u7f51\u7ad9')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('status', models.PositiveIntegerField(choices=[(1, '\u6b63\u5e38'), (0, '\u5220\u9664')], default=1, verbose_name='\u72b6\u6001')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='\u8bc4\u8bba\u76ee\u6807')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
