# Generated by Django 3.2.4 on 2021-07-04 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0022_coownerlitigation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coownerlitigation',
            name='coownerheir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coownerlitigatiions', to='yfcases.coownerheir'),
        ),
    ]
