# Generated by Django 4.2.4 on 2023-09-06 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student_details',
            new_name='student_detail',
        ),
    ]