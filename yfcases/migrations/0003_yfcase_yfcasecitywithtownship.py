# Generated by Django 3.2.4 on 2021-06-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0002_result_casestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseCityWithTownship',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='縣市鄉鎮'),
        ),
    ]