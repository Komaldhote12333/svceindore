# Generated by Django 4.0.1 on 2023-09-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_course_fees_subcollege_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='role',
            field=models.CharField(max_length=100, null=True),
        ),
    ]