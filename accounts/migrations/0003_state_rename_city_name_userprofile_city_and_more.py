# Generated by Django 4.1.7 on 2023-04-09 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_age_alter_userprofile_city_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_title', models.CharField(max_length=100)),
                ('state_description', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='city_name',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('districtid', models.AutoField(primary_key=True, serialize=False)),
                ('district_title', models.CharField(max_length=100)),
                ('district_description', models.CharField(max_length=100)),
                ('district_status', models.CharField(max_length=10)),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.state')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('districtid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.districts')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.state')),
            ],
        ),
    ]
