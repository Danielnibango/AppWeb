# Generated by Django 5.2 on 2025-06-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0005_paiement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='heure',
            field=models.FloatField(default=0),
        ),
    ]
