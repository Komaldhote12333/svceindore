# Generated by Django 4.0.1 on 2023-08-30 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_achievements_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentplacement',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placedstudentclg', to='app.college'),
        ),
    ]
