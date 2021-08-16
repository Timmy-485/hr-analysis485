# Generated by Django 3.2.6 on 2021-08-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_size', models.CharField(choices=[('<10', 'less than 10'), ('10/49', '10 to 49'), ('50-99', '50 to 99'), ('100-500', '100 to 500'), ('500-599', '500 to 599'), ('1000-4999', '1000 to 4999'), ('5000-9999', '5000 to 9999'), ('10000+', 'more than 10000')], default='<10', max_length=20)),
                ('edu_level', models.CharField(choices=[('Graduate', 'Graduate'), ('Masters', 'Masters'), ('High School', 'High School'), ('Phd', 'Phd'), ('Primary School', 'Primary School')], default='Graduate', max_length=20)),
                ('major', models.CharField(choices=[('STEM', 'STEM'), ('Business Degree', 'Business Degree'), ('No Major', 'No Major'), ('Arts', 'Arts'), ('Humanities', 'Humanities'), ('Other', 'Other')], default='No Major', max_length=20)),
                ('company_type', models.CharField(choices=[('Pvt Ltd', 'Pvt Ltd'), ('Funded Startup', 'Funded Startup'), ('Early Stage Startup', 'Early Stage Startup'), ('Other', 'Other'), ('Public Sector', 'Public Sector'), ('NGO', 'NGO')], default='Public Sector', max_length=20)),
                ('experience', models.CharField(choices=[('Has relevent experience', 'Has relevent experience'), ('No relevent experience', 'No relevent experience')], default='No relevent experience', max_length=30)),
            ],
        ),
    ]
