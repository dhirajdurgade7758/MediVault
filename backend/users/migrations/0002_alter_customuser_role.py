# Generated by Django 5.2 on 2025-04-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor'), ('admin', 'Admin')], default='patient', max_length=10),
        ),
    ]
