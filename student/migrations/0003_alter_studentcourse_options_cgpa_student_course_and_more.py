# Generated by Django 4.0.6 on 2022-07-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_course_profile_studentcourse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentcourse',
            options={'verbose_name': 'Student Course', 'verbose_name_plural': 'Student Courses'},
        ),
        migrations.AddField(
            model_name='cgpa',
            name='student_course',
            field=models.ManyToManyField(to='student.studentcourse'),
        ),
        migrations.AlterModelTable(
            name='studentcourse',
            table=None,
        ),
    ]