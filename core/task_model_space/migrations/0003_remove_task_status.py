# Generated by Django 5.0.2 on 2024-02-15 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_model_space', '0002_alter_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
