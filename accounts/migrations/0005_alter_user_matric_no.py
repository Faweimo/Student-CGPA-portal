# Generated by Django 4.0.6 on 2022-07-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_matric_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matric_no',
            field=models.CharField(default='2022/52/978AC', max_length=50, unique=True),
        ),
    ]