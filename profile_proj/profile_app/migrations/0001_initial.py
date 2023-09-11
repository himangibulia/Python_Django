# Generated by Django 4.2.4 on 2023-09-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('mobile_no', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=6)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
