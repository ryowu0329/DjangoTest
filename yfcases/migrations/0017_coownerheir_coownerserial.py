# Generated by Django 3.2.4 on 2021-07-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0016_coownerheir'),
    ]

    operations = [
        migrations.AddField(
            model_name='coownerheir',
            name='coOwnerSerial',
            field=models.DecimalField(blank=True, decimal_places=0, default=1, max_digits=82, null=True, verbose_name='順位'),
        ),
    ]
