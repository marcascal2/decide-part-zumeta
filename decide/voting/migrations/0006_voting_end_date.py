# Generated by Django 2.0 on 2020-12-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_remove_voting_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]