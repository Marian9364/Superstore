# Generated by Django 4.1.3 on 2022-12-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_first_name_alter_appuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('diverse', 'Diverse')], max_length=7),
        ),
    ]
