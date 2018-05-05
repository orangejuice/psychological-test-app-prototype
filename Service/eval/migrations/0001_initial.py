# Generated by Django 2.0.4 on 2018-05-05 09:59

import django.db.models.deletion
from django.db import migrations, models

import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='static/images/thumb')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'eval_scale',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ScaleConclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'eval_conclusion',
            },
        ),
        migrations.CreateModel(
            name='ScaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(default=1)),
                ('question', models.TextField()),
            ],
            options={
                'db_table': 'eval_item',
                'ordering': ['sn'],
            },
        ),
        migrations.CreateModel(
            name='ScaleItemOpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'eval_item_opts',
            },
        ),
        migrations.CreateModel(
            name='ScaleOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(default=1)),
                ('value', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'eval_option',
            },
        ),
        migrations.CreateModel(
            name='ScaleRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chose', jsonfield.fields.JSONField(verbose_name='已选')),
                ('score', jsonfield.fields.JSONField(verbose_name='最终得分')),
                ('result', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Scale')),
            ],
            options={
                'db_table': 'eval_record',
            },
        ),
        migrations.CreateModel(
            name='ScaleResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Scale')),
            ],
            options={
                'db_table': 'eval_result',
            },
        ),
    ]
