# Generated by Django 4.2.4 on 2023-09-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_student_detail_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='pin_code',
            field=models.IntegerField(max_length=6),
        ),
    ]