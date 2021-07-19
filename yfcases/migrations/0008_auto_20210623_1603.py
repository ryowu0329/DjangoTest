# Generated by Django 3.2.4 on 2021-06-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0007_auto_20210623_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseAcceptingAuthorityTownship',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='鄉鎮區里'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseApplyAcrossInstitutions',
            field=models.BooleanField(default=False, verbose_name='跨所申請'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseRealEstateRegistrationDateOfCause',
            field=models.DateField(blank=True, null=True, verbose_name='原因發生日期'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseRealEstateRegistrationReasonForRegistration',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='登記原因'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseRealEstateRegistrationRegisteredAgent',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='登記代理人'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseRealEstateRegistrationRegistrationNote',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='登記備註'),
        ),
    ]
