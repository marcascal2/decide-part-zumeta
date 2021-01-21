# Generated by Django 2.0 on 2021-01-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0034_remove_voting_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='lugares',
            field=models.TextField(choices=[('AN', 'Andalucia'), ('AR', 'Aragon'), ('AS', 'Asturias'), ('BA', 'Baleares'), ('CA', 'Canarias'), ('CT', 'Cantabria'), ('CAM', 'Castilla-Mancha'), ('CAL', 'Castilla-Leon'), ('CAT', 'Cataluña'), ('CE', 'Ceuta'), ('EX', 'Extremadura'), ('GA', 'Galicia'), ('LR', 'La-Rioja'), ('MA', 'Madrid'), ('ME', 'Melilla'), ('MU', 'Murcia'), ('NA', 'Navarra'), ('PV', 'País-Vasco'), ('VA', 'Valencia')], default='AN'),
        ),
    ]