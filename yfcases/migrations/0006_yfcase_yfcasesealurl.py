# Generated by Django 3.2.4 on 2021-06-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0005_auto_20210620_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseSealUrl',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
