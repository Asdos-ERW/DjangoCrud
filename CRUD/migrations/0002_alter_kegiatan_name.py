# Generated by Django 4.0.6 on 2022-08-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegiatan',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
