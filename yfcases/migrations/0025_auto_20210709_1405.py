# Generated by Django 3.2.4 on 2021-07-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0024_alter_coownerlitigation_coownerheir'),
    ]

    operations = [
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseCownerAgent',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='共有人代理人'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcasecoOwnerBuildHPAll',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='建物所有持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcasecoOwnerBuildHPPersonnal',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='建物個人持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcasecoOwnerLandHPAll',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地所有持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcasecoOwnerLandHPPersonnal',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地個人持分'),
        ),
    ]
