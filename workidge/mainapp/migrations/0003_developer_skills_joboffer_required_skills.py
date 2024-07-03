# Generated by Django 5.0.6 on 2024-07-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_person_is_staff_person_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='skills',
            field=models.ManyToManyField(related_name='developers', to='mainapp.competence'),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='required_skills',
            field=models.ManyToManyField(related_name='job_offers', to='mainapp.competence'),
        ),
    ]
