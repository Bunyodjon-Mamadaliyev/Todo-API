# Generated by Django 5.2 on 2025-04-19 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='task_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_uz',
            field=models.TextField(null=True),
        ),
    ]
