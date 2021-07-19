# Generated by Django 3.2.4 on 2021-06-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0006_yfcase_yfcasesealurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferArea1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='移轉情形-面積(平方公尺)-1'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferArea2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='移轉情形-面積(平方公尺)-2'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferArea3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='移轉情形-面積(平方公尺)-3'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferArea4',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='移轉情形-面積(平方公尺)-4'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferArea5',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='移轉情形-面積(平方公尺)-5'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferArea6',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='移轉情形-面積(平方公尺)-6'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferLevel1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-層次1'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferLevel2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-層次2'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferLevel3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-層次3'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferLevel4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-層次4'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferLevel5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-層次5'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferLevel6',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-層次6'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicBuildingNumber1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-公設建號1'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicBuildingNumber2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-公設建號2'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicBuildingNumber3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-公設建號3'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicBuildingNumber4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-公設建號4'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicHoldings1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-持分比例1'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicHoldings2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-持分比例2'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicHoldings3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-持分比例3'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferPublicHoldings4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-持分比例4'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferStructure1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-構造1'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferStructure2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-構造2'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferStructure3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-構造3'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferStructure4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-構造4'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferStructure5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-構造5'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxBuildingTransferStructure6',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='移轉情形-構造6'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxClient',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='契稅委託人'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxClosingNewsletter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='契稅結案簡訊'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCoOwnerMatch',
            field=models.BooleanField(default=True, verbose_name='共有人一致'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorAlley',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='弄'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorBirthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorBuildHoldingPointAll',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='建物所有持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorBuildHoldingPointPersonal',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='建物個人持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorCity',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='縣市'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorFloor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='樓(含之幾)'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorIdentityCard',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='身分証或統一編號'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorLandHoldingPointAll',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地所有持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorLandHoldingPointPersonal',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地個人持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorLane',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='巷'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorLocalPhone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='市話'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorMobilePhone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='手機'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorNeighbor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='鄰'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorNumber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='號'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorSection',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='段'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorStreet',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='街路'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorTownship',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='鄉鎮區'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxCreditorVillage',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='村里'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorAlley',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='弄'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorBirthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorBuildHoldingPointAll',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='建物所有持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorBuildHoldingPointPersonal',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='建物個人持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorCity',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='縣市'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorFloor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='樓(含之幾)'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorIdentityCard',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='身分証或統一編號'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorLandHoldingPointAll',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地所有持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorLandHoldingPointPersonal',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地個人持分'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorLane',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='巷'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorLocalPhone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='市話'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorMobilePhone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='手機'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorNeighbor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='鄰'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorNumber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='號'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorSection',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='段'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorStreet',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='街路'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorTownship',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='鄉鎮區'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDebtorVillage',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='村里'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxDeclarationDate',
            field=models.DateField(blank=True, null=True, verbose_name='契稅申報日期'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxEstablishmentDate',
            field=models.DateField(blank=True, null=True, verbose_name='契稅建立日期'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxHouseTaxRegistrationNumber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='房屋稅籍編號'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxReclaimMethod',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='契稅領回方式'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxRemarks',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='契稅備註'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxReportAttached',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='契稅報附聯'),
        ),
        migrations.AddField(
            model_name='yfcase',
            name='yfcaseDeedtaxTransferPrice',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='契稅移轉價格'),
        ),
    ]
