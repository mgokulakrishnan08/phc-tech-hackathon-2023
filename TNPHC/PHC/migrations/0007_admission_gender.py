# Generated by Django 4.1.7 on 2023-03-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PHC', '0006_admission_age_admission_blood_group_admission_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='gender',
            field=models.CharField(max_length=11, null=True),
        ),
    ]