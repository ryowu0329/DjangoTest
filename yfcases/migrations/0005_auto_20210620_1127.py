# Generated by Django 3.2.4 on 2021-06-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0004_yfcase_yfcasecasestatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='caseStatus',
        ),
        migrations.AlterField(
            model_name='yfcase',
            name='yfcaseCreditor',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='債權人'),
        ),
        migrations.AlterField(
            model_name='yfcase',
            name='yfcaseDebtor',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='債務人'),
        ),
    ]
