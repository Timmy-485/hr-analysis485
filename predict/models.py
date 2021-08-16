from django.db import models

# Create your models here.
class PredictionResults(models.Model):
    training_hours = models.IntegerField(default=0)
    city_dev_index = models.FloatField(default=0)
    experience = models.IntegerField(default=0)
    last_new_job = models.IntegerField(default=0)

    less_than_10 = '<10'
    ten_to_49 = '10/49'
    fifty_to_99 = '50-99'
    hundred_to_500 = '100-500'
    fivehundred_to_599 = '500-999'
    thousand_to_4999 = '1000-4999'
    fivethousand_to_9999 = '5000-9999'
    more_than_10000 = '10000+'
    size_choices = [
        (less_than_10, 'less than 10'),
        (ten_to_49, '10 to 49'),
        (fifty_to_99, '50 to 99'),
        (hundred_to_500,  '100 to 500'),
        (fivehundred_to_599, '500 to 999'),
        (thousand_to_4999, '1000 to 4999'),
        (fivethousand_to_9999, '5000 to 9999'),
        (more_than_10000, 'more than 10000')
    ]
    company_size = models.CharField(max_length=20, choices=size_choices, default=less_than_10)

    graduate = 'Graduate'
    masters = 'Masters'
    high_school = 'High School'
    phd = 'Phd'
    primary = 'Primary School'
    edu_level_choices = [
        (graduate, 'Graduate'),
        (masters, 'Masters'),
        (high_school, 'High School'),
        (phd, 'Phd'),
        (primary, 'Primary School')
    ]
    edu_level = models.CharField(max_length=20, choices=edu_level_choices, default=graduate)

    stem = 'STEM'
    business = 'Business Degree'
    no_major = 'No Major'
    arts = 'Arts'
    humanities = 'Humanities'
    other = 'Other'
    major_choices = [
        (stem, 'STEM'),
        (business, 'Business Degree'),
        (no_major, 'No Major'),
        (arts, 'Arts'),
        (humanities, 'Humanities'),
        (other, 'Other'),
    ]
    major = models.CharField(max_length=20, choices=major_choices, default=no_major) 

    private = 'Pvt Ltd'
    funded = 'Funded Startup'
    early_startup = 'Early Stage Startup'
    other = 'Other'
    public = 'Public Sector'
    ngo = 'NGO'
    company_type_choices = [
        (private, 'Pvt Ltd'),
        (funded, 'Funded Startup'),
        (early_startup, 'Early Stage Startup'),
        (other, 'Other'),
        (public, 'Public Sector'),
        (ngo, 'NGO')
    ]
    company_type = models.CharField(max_length=20, choices=company_type_choices, default=public) 

    has_exp = 'Has relevent experience'
    no_exp = 'No relevent experience'
    experience_choices = [
        (has_exp, 'Has relevent experience'),
        (no_exp, 'No relevent experience')
    ]
    relevant_experience = models.CharField(max_length=30, choices=experience_choices, default=no_exp) 

    
    prediction_result = models.IntegerField(default=0)
