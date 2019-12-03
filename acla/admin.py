from django.contrib import admin
from .models import Suspicious
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Suspicious)
class AclAdmin(ImportExportModelAdmin):
    list_display = ['AC_NO','status',	'ac_name',	'AC_BRANCH',	'AC_CCY',	'LCY_AMOUNT',	'VALUE_DT',	'AC_STAT_NO_DR', 'ACCOUNT_CLASS', 'RECORD_STAT',	'CUST_NO',	'TotalTnx',	'serviceDesc',	'OnboardDate',	'msisdn',	'eAlertTelPhone']
    list_filter = ['VALUE_DT', 'ACCOUNT_CLASS','status']
    search_fields = ['AC_NO', 'AC_NAME','AC_BRANCH', 'VALUE_DT','CUST_NO']