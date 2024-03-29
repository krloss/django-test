# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
                ('voto', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('data', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='escolha',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Questao'),
        ),
    ]
