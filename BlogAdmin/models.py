from django.db import models

class TUser(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)
    name = models.CharField(db_column='Name',max_length=20,blank=True,null=True)
    pwd = models.CharField(db_column='Pwd',max_length=100,blank=True,null=True)
    mail = models.CharField(db_column='Mail',max_length=50,blank=True,null=True)
    phone = models.CharField(db_column='Phone',max_length=20,blank=True,null=True)
    address = models.CharField(db_column='Address',max_length=200,blank=True,null=True)
    logintime = models.DateTimeField(db_column='LoginTime',blank=True,null=True)
    loginip = models.CharField(db_column='LoginIp',max_length=20,blank=True,null=True)
    previp = models.CharField(db_column='PrevIp', max_length=20, blank=True, null=True)
    count = models.IntegerField(db_column='Count',blank=True,default=0)

    class Meta:
        db_table = 't_user'

