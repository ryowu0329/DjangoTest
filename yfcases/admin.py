from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
  
# admin.site.register(Yfcase)
# admin.site.register(City)
# admin.site.register(Township)
admin.site.register(Land)
admin.site.register(Build)
admin.site.register(FinalDecision)

@admin.register(Yfcase)
class YfcaseAdmin(ImportExportModelAdmin):
  list_display=('id','yfcaseCaseNumber','yfcaseCompany','yfcaseCity','yfcaseTownship','yfcaseBigSection','yfcaseSmallSection',"yfcaseVillage","yfcaseNeighbor","yfcaseStreet","yfcaseSection","yfcaseLane","yfcaseAlley","yfcaseNumber","yfcaseFloor",'yfcaseDebtor','yfcaseCreditor','yfcaseCreditorMobilePhone','yfcaseCityWithTownship','yfcaseCaseStatus','user')
  pass

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
  list_display=('id','name')

@admin.register(Township)
class TownshipAdmin(ImportExportModelAdmin):
  list_display=('id',"city","name","zip_code","district_court","land_office","finance_and_tax_bureau","police_station","irs","home_office")
  pass