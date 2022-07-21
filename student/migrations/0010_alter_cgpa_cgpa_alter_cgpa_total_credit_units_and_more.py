# Generated by Django 4.0.6 on 2022-07-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_remove_cgpa_profile_cgpa_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cgpa',
            name='cgpa',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='cgpa',
            name='total_credit_units',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cgpa',
            name='total_unit_points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
