# Generated by Django 4.1.7 on 2023-04-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('Approved', 'APPROVED'), ('deliver', 'DELIVER'), ('completed', 'COMPLETED')], default='pending', max_length=50),
        ),
    ]
