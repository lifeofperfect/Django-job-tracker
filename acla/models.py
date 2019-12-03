from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL
# Create your models here.
class Suspicious(models.Model):
    AC_NO = models.CharField(max_length=15)
    ac_name = models.CharField(max_length=200)
    AC_BRANCH = models.CharField(max_length=4)
    AC_CCY = models.CharField(max_length=4)
    FCY_AMOUNT = models.IntegerField(null=True)
    LCY_AMOUNT = models.IntegerField(blank=False)
    VALUE_DT = models.CharField(max_length=10, blank=True)
    AC_STAT_NO_DR = models.CharField(max_length=2)
    ACCOUNT_CLASS = models.CharField(max_length=10)
    ACY_AVL_BAL = models.IntegerField(null=True)
    RECORD_STAT = models.CharField(max_length=1)
    CUST_NO = models.IntegerField()
    min_balance = models.IntegerField(null=True)
    TotalTnx = models.IntegerField(null=True)
    serviceDesc = models.CharField(max_length=100, default='none')
    OnboardDate = models.CharField(null=True, max_length=20)
    msisdn = models.CharField(max_length=18, null=True)
    eAlertTelPhone = models.CharField(max_length=20, null=True)

    choices = (
        ('TRUE POSITIVE', 'TRUE POSITIVE'),
        ('FALSE POSITIVE', 'FALSE POSITIVE'),
        ('UNDEFINED', 'UNDEFINED')
    )

    status = models.CharField(choices=choices, default='UNDEFINED', max_length=20)
    comment = models.TextField(max_length=30, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    edit_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,default=1,null=True, on_delete=models.SET_NULL )


    class Meta:
        ordering=['-id']

    def get_absolute_url(self):
        return f"/alert/{self.id}"

    def __str__(self):
        return self.AC_NO + ' ' + self.ac_name
