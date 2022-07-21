# Generated by Django 4.0.6 on 2022-07-18 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_matric_no'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='profile',
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.result')),
            ],
            options={
                'verbose_name': 'Student Course',
                'verbose_name_plural': 'Student Courses',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
