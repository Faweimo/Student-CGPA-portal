# Generated by Django 4.0.6 on 2022-07-21 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_matric_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matric_no',
            field=models.CharField(default='2022/24/144AB', max_length=50, unique=True),
        ),
    ]