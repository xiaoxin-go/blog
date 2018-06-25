from django.db import models

# Create your models here.

class TContent(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)
    user = models.CharField(db_column='User',max_length=50,blank=True,null=True)
    title = models.CharField(db_column='Title',max_length=100,blank=True,null=True)
    read = models.IntegerField(db_column='Read',blank=True,null=True,default=0)
    review = models.IntegerField(db_column='Review',blank=True,null=True,default=0)
    addTime = models.DateTimeField(db_column='AddTime',blank=True,null=True)
    content = models.TextField(db_column='Content',blank=True,null=True)
    label = models.CharField(db_column='Label',max_length=100,blank=True,null=True)
    isdelete = models.IntegerField(db_column='IsDelete',blank=True,null=True,default=1)
    type = models.IntegerField(db_column='Type',blank=True,null=True,default=0)
    img = models.CharField(db_column='Img',max_length=50,blank=True,null=True)
    class Meta:
        db_table = 't_content'

class TLink(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)
    name = models.CharField(db_column='Name',max_length=100,blank=True,null=True)
    link = models.CharField(db_column='Link',max_length=150,blank=True,null=True)
    isdelete = models.IntegerField(db_column='IsDelete',blank=True,null=True,default=1)

    class Meta:
        db_table = 't_link'

class TImage(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)
    name = models.CharField(db_column='Name',max_length=100,blank=True,null=True)
    isdelete = models.IntegerField(db_column='IsDelete',blank=True,null=True,default=1)

    class Meta:
        db_table = 't_image'

class TMood(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)
    addTime = models.DateTimeField(db_column='AddTime',blank=True,null=True)
    text = models.TextField(db_column='Text',blank=True,null=True)
    isdelete = models.IntegerField(db_column='IsDelete',blank=True,null=True,default=1)
    img = models.CharField(db_column='Img',max_length=50,blank=True,null=True)

    class Meta:
        db_table = 't_mood'

class TComment(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)
    addTime = models.DateTimeField(db_column='AddTime',blank=True,null=True)
    text = models.TextField(db_column='Text',blank=True,null=True)
    isdelete = models.IntegerField(db_column='IsDelete',blank=True,default=1)
    countid = models.IntegerField(db_column='CountId')
