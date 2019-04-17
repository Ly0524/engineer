from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    class Meta:
        db_table='userinfo'

class Pic(models.Model):
    pname=models.CharField(max_length=50)
    ppassword=models.CharField(max_length=20)
    pinstitute=models.CharField(max_length=50)
    class Meta:
        db_table='pic'

class SafeUser(models.Model):
    sname=models.CharField(max_length=50)
    spassword=models.CharField(max_length=20)
    sinstitute=models.CharField(max_length=50)
    p=models.ForeignKey("Pic",'id')
    class Meta:
        db_table='safeuser'

class Work(models.Model):
    wengineer_name=models.CharField(max_length=50)
    wengineer_num=models.CharField(max_length=50)
    wlinkman=models.CharField(max_length=50)
    wphone=models.CharField(max_length=12)
    class Meta:
        db_table='work'

class NotifyInfo(models.Model):
    GENDER_CHOICE={
        (u'Car',u'车辆违规信息'),
        (u'Person', u'人员违规信息'),
        (u'Other',u'其他违规信息'),
    }
    errortype=models.CharField(max_length=20,choices=GENDER_CHOICE)
    CHULI_CHOICE={
        (u'N',u'未处理'),
        (u'T', u'处理中'),
        (u'Y', u'已处理')
    }
    dealvalue=models.CharField(max_length=20,choices=CHULI_CHOICE)
    createTime=models.DateTimeField(auto_now_add=True)
    changeTime=models.DateTimeField(auto_now=True)
    s=models.ForeignKey("SafeUser",'id')
    w=models.ForeignKey("Work",'id')
    class Meta:
        db_table='notifyinfo'



