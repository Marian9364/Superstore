# Generated by Django 4.1.3 on 2022-12-01 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0003_alter_toy_toy_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('to_toy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.toy')),
            ],
        ),
    ]
