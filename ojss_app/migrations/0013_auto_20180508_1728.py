# Generated by Django 2.0.4 on 2018-05-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0012_application_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='name',
            new_name='seeker_name',
        ),
    ]
