# Generated by Django 4.2.4 on 2023-09-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_remove_student_detail_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_detail',
            name='mobile_no',
            field=models.IntegerField(default=10, max_length=10),
            preserve_default=False,
        ),
    ]
