# Generated by Django 2.2 on 2019-04-09 11:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNum', models.CharField(max_length=20)),
                ('iname', models.CharField(max_length=8)),
                ('addTime', models.DateField(default=datetime.date.today)),
            ],
            options={
                'unique_together': {('cardNum', 'iname')},
            },
        ),
        migrations.CreateModel(
            name='ZhongBen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseCode', models.CharField(max_length=64)),
                ('sexy', models.CharField(max_length=8)),
                ('regDate', models.CharField(max_length=32)),
                ('courtName', models.CharField(max_length=32)),
                ('execMoney', models.CharField(max_length=16)),
                ('finalDate', models.CharField(max_length=32)),
                ('unperformMoney', models.CharField(max_length=16)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zb', to='zxgkInfo.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Xgl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courtName', models.CharField(max_length=32)),
                ('sexy', models.CharField(max_length=8)),
                ('regDate', models.CharField(max_length=32)),
                ('caseCode', models.CharField(max_length=64)),
                ('areaName', models.CharField(max_length=32)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='xg', to='zxgkInfo.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ShiXin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaName', models.CharField(max_length=32)),
                ('sexy', models.CharField(max_length=8)),
                ('caseCode', models.CharField(max_length=64)),
                ('courtName', models.CharField(max_length=32)),
                ('disruptTypeName', models.CharField(max_length=64)),
                ('duty', models.TextField()),
                ('gistId', models.CharField(max_length=32)),
                ('gistUnit', models.CharField(max_length=32)),
                ('performance', models.CharField(max_length=32)),
                ('publishDate', models.CharField(max_length=32)),
                ('regDate', models.CharField(max_length=32)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sx', to='zxgkInfo.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Bzxr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courtName', models.CharField(max_length=32)),
                ('sexy', models.CharField(max_length=8)),
                ('regDate', models.CharField(max_length=32)),
                ('caseCode', models.CharField(max_length=64)),
                ('execMoney', models.CharField(max_length=16)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bzxr', to='zxgkInfo.Person')),
            ],
        ),
    ]
