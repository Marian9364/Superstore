# Generated by Django 4.1.3 on 2022-12-01 10:15

from django.db import migrations, models
import superstore.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_toy_toy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='toy_photo',
            field=models.ImageField(upload_to='', validators=[superstore.photos.validators.validate_file_size]),
        ),
    ]