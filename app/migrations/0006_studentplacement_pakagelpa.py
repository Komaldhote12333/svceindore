# Generated by Django 4.0.1 on 2023-08-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_studentplacement_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentplacement',
            name='pakageLpa',
            field=models.CharField(default='', max_length=100),
        ),
    ]