# Generated by Django 4.0.1 on 2023-08-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='image',
            field=models.ImageField(default='', upload_to='Achiements/'),
        ),
        migrations.AddField(
            model_name='buses',
            name='image',
            field=models.ImageField(default='', upload_to='Bus/'),
        ),
        migrations.AddField(
            model_name='canteen',
            name='image',
            field=models.ImageField(default='', upload_to='Cantten/'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(default='', upload_to='Faculty/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='', upload_to='Gallery/'),
        ),
        migrations.AddField(
            model_name='sportimages',
            name='image',
            field=models.ImageField(default='', upload_to='Sport/'),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='image',
            field=models.ImageField(default='', upload_to='Placedstudent/'),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='studentname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='', upload_to='Events/'),
        ),
    ]
