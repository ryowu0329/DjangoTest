# Generated by Django 3.2.4 on 2021-06-18 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='城市')),
            ],
            options={
                'db_table': 'yfcase_city',
            },
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='鄉鎮')),
                ('zip_code', models.CharField(max_length=30, verbose_name='郵遞區號')),
                ('district_court', models.CharField(max_length=30, verbose_name='地方法院')),
                ('land_office', models.CharField(max_length=30, verbose_name='地政事務所')),
                ('finance_and_tax_bureau', models.CharField(max_length=30, verbose_name='財政稅務局')),
                ('police_station', models.CharField(max_length=30, verbose_name='警察局')),
                ('irs', models.CharField(max_length=30, verbose_name='國稅局')),
                ('home_office', models.CharField(max_length=30, verbose_name='戶政事務所')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yfcases.city')),
            ],
            options={
                'db_table': 'yfcase_township',
            },
        ),
        migrations.CreateModel(
            name='Yfcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yfcaseCaseNumber', models.CharField(max_length=100, verbose_name='案號(*)')),
                ('yfcaseCompany', models.CharField(blank=True, max_length=50, null=True, verbose_name='所屬公司')),
                ('yfcaseBigSection', models.CharField(blank=True, max_length=10, null=True, verbose_name='段號')),
                ('yfcaseSmallSection', models.CharField(blank=True, max_length=10, null=True, verbose_name='小段')),
                ('yfcaseVillage', models.CharField(blank=True, max_length=100, null=True, verbose_name='村里')),
                ('yfcaseNeighbor', models.CharField(blank=True, max_length=100, null=True, verbose_name='鄰')),
                ('yfcaseStreet', models.CharField(blank=True, max_length=100, null=True, verbose_name='街路')),
                ('yfcaseSection', models.CharField(blank=True, max_length=100, null=True, verbose_name='段')),
                ('yfcaseLane', models.CharField(blank=True, max_length=100, null=True, verbose_name='巷')),
                ('yfcaseAlley', models.CharField(blank=True, max_length=100, null=True, verbose_name='弄')),
                ('yfcaseNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='號')),
                ('yfcaseFloor', models.CharField(blank=True, max_length=100, null=True, verbose_name='樓(含之幾)')),
                ('yfcaseDebtor', models.CharField(blank=True, max_length=10, null=True, verbose_name='債務人')),
                ('yfcaseCreditor', models.CharField(blank=True, max_length=10, null=True, verbose_name='債權人')),
                ('yfcaseCreditorMobilePhone', models.CharField(blank=True, max_length=20, null=True, verbose_name='債權人電話')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='區域負責人')),
                ('yfcaseCity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yfcases.city', verbose_name='縣市')),
                ('yfcaseTownship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yfcases.township', verbose_name='鄉鎮區里')),
            ],
            options={
                'db_table': 'yfcase_yfcase',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyFirstDay', models.CharField(blank=True, max_length=100, null=True, verbose_name='初勘日')),
                ('surveySecondDay', models.CharField(blank=True, max_length=100, null=True, verbose_name='會勘日')),
                ('surveyForeclosureAnnouncementLink', models.URLField(blank=True, null=True, verbose_name='法拍公告(證物三)')),
                ('survey988Link', models.URLField(blank=True, null=True, verbose_name='998連結')),
                ('surveyObjectPhotoLink', models.URLField(blank=True, null=True, verbose_name='物件照片(證物四)')),
                ('surveyNetMarketPriceLink', models.URLField(blank=True, null=True)),
                ('surveyForeclosureRecordLink', models.URLField(blank=True, null=True, verbose_name='法拍記錄(證物七)')),
                ('surveyObjectViewLink', models.URLField(blank=True, max_length=500, null=True, verbose_name='標的物(現場勘查)')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopBuyDate', models.CharField(blank=True, max_length=20, null=True, verbose_name='一買止日')),
                ('actionResult', models.CharField(blank=True, max_length=20, null=True, verbose_name='執行結果')),
                ('bidAuctionTime', models.CharField(blank=True, max_length=20, null=True, verbose_name='搶標拍別')),
                ('bidMoney', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='搶標金額')),
                ('objectNumber', models.CharField(blank=True, max_length=20, null=True, verbose_name='標的編號')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectBuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectBuildAddress', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('objectBuildTotalPrice', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='總價(NT)')),
                ('objectBuildBuildArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='建坪(坪)')),
                ('objectBuildHouseAge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='屋齡(年)')),
                ('objectBuildFloorHeight', models.CharField(blank=True, max_length=100, null=True, verbose_name='樓高')),
                ('objectBuildStatus', models.CharField(blank=True, max_length=100, null=True, verbose_name='狀態')),
                ('objectBuildTransactionDate', models.CharField(blank=True, max_length=100, null=True, verbose_name='成交日期')),
                ('objectBuildUrl', models.URLField(blank=True, null=True, verbose_name='附件')),
                ('objectBuildScorerA', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員A')),
                ('objectBuildScorerB', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員B')),
                ('objectBuildScorerC', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員C')),
                ('objectBuildScorRateA', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成A')),
                ('objectBuildScorRateB', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成B')),
                ('objectBuildScorRateC', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成C')),
                ('objectBuildScorReasonA', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因A')),
                ('objectBuildScorReasonB', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因B')),
                ('objectBuildScorReasonC', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因C')),
                ('plusItemA1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherA', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueA1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherA', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusItemB1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherB', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueB1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherB', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusItemC1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemC5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherC', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueC1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueC5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherC', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectbuilds', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='地號')),
                ('landUrl', models.URLField(blank=True, null=True, verbose_name='謄本')),
                ('landArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='地坪(平方公尺)')),
                ('landHoldingPointPersonal', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='個人持分')),
                ('landHoldingPointAll', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='所有持分')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lands', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='FinalDecision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalDecision', models.CharField(blank=True, max_length=10, null=True, verbose_name='最終判定')),
                ('finalDecisionRemark', models.CharField(blank=True, max_length=100, null=True, verbose_name='備註')),
                ('regionalHead', models.CharField(blank=True, max_length=10, null=True, verbose_name='區域負責人')),
                ('regionalHeadDate', models.CharField(blank=True, max_length=10, null=True, verbose_name='區域負責人簽核日期')),
                ('regionalHeadWorkArea', models.CharField(blank=True, max_length=10, null=True, verbose_name='區域負責人轄區')),
                ('subSigntrueA', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署人員A')),
                ('subSigntrueDateA', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署日期A')),
                ('subSigntrueWorkAreaA', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署轄區A')),
                ('subSigntrueB', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署人員B')),
                ('subSigntrueDateB', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署日期B')),
                ('subSigntrueWorkAreaB', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署轄區B')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finaldecisions', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='建號')),
                ('buildUrl', models.URLField(blank=True, null=True, verbose_name='謄本')),
                ('buildArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='建坪(平方公尺)')),
                ('buildHoldingPointPersonal', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='個人持分')),
                ('buildHoldingPointAll', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='所有持分')),
                ('buildTypeUse', models.CharField(blank=True, max_length=100, null=True, verbose_name='建物型')),
                ('buildUsePartition', models.CharField(blank=True, max_length=100, null=True, verbose_name='使用分區')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctionDateFirst', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第一拍)')),
                ('auctionDateSecond', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第二拍)')),
                ('auctionDateThird', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第三拍)')),
                ('auctionDateFourth', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第四拍)')),
                ('auctionFloorPriceFirst', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第一拍)')),
                ('auctionFloorPriceSecond', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第二拍)')),
                ('auctionFloorPriceThird', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第三拍)')),
                ('auctionFloorPriceFourth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第四拍)')),
                ('auctionClickFirst', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第一拍)')),
                ('auctionClickSecond', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第二拍)')),
                ('auctionClickThird', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第三拍)')),
                ('auctionClickFourth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第四拍)')),
                ('auctionMonitorFirst', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第一拍)')),
                ('auctionMonitorSecond', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第二拍)')),
                ('auctionMonitorThird', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第三拍)')),
                ('auctionMonitorFourth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第四拍)')),
                ('auctionMarginFirst', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第一拍)')),
                ('auctionMarginSecond', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第二拍)')),
                ('auctionMarginThird', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第三拍)')),
                ('auctionMarginFourth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第四拍)')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='yfcases.yfcase')),
            ],
        ),
    ]