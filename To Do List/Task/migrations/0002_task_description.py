# Generated by Django 5.0.3 on 2024-08-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
