# Generated by Django 3.2 on 2021-05-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaverequest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavedetails',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='leavedetails',
            name='startDate',
            field=models.DateField(null=True),
        ),
    ]
