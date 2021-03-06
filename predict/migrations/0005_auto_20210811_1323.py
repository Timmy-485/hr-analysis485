# Generated by Django 3.2.6 on 2021-08-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0004_alter_predictionresults_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictionresults',
            name='relevant_experience',
            field=models.CharField(choices=[('Has relevent experience', 'Has relevent experience'), ('No relevent experience', 'No relevent experience')], default='No relevent experience', max_length=30),
        ),
        migrations.AlterField(
            model_name='predictionresults',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]
