# Generated by Django 2.0 on 2020-12-28 20:45

from django.db import migrations, models
import voting.models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, validators=[voting.models.validate_start_date]),
        ),
    ]
