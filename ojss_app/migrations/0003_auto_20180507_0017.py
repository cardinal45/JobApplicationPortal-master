# Generated by Django 2.0.4 on 2018-05-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0002_seekerprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofile',
            name='birthDate',
            field=models.DateField(),
        ),
    ]
