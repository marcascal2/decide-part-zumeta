# Generated by Django 2.0 on 2020-12-28 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.PositiveIntegerField(blank=True, null=True)),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('option', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_options', to='voting.Question')),
            ],
        ),
    ]
