# Generated by Django 3.0.3 on 2022-01-09 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_mobile_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sur_name',
            new_name='surname',
        ),
    ]
