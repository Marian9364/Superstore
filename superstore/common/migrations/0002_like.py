# Generated by Django 4.1.3 on 2022-12-01 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_toy_toy_photo'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_toy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.toy')),
            ],
        ),
    ]
