# Generated by Django 4.0.1 on 2023-09-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_studentplacement_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='fees',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subcollege',
            name='duration',
            field=models.CharField(max_length=100, null=True),
        ),
    ]