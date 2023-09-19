# Generated by Django 4.0.1 on 2023-09-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_eventimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Events_images2/')),
            ],
        ),
        migrations.RemoveField(
            model_name='eventimages',
            name='image',
        ),
        migrations.AddField(
            model_name='eventimages',
            name='images',
            field=models.ManyToManyField(to='app.Image'),
        ),
    ]
