# Generated by Django 4.0.1 on 2023-09-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_courseimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='Aboutprincipal',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='hprincipaldimg',
            field=models.ImageField(null=True, upload_to='principalimg/'),
        ),
        migrations.AddField(
            model_name='college',
            name='principalname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='aboutdepartment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='hoddetais',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='hodimg',
            field=models.ImageField(null=True, upload_to='hodimg/'),
        ),
        migrations.AddField(
            model_name='course',
            name='hodname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
