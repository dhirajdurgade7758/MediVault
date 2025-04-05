# Generated by Django 5.2 on 2025-04-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=255)),
                ('diagnosis_code', models.CharField(max_length=100)),
                ('treatment_date', models.DateField()),
                ('claim_amount', models.FloatField()),
                ('status', models.CharField(default='pending', max_length=50)),
            ],
        ),
    ]
