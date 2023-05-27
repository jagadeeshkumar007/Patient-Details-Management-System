from django.db import models
from datetime import datetime
# Create your models here.
class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
class product(models.Model):
    username=models.CharField(max_length=100)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)

    def __str__(self):
        return self.username
class adhar(models.Model):
    ad_no=models.CharField(max_length=12,)
    #email=models.CharField(max_length=12)
    #passwdad_no=models.CharField(max_length=12)
    def __str__(self):
        return self.ad_no
class hospitals(models.Model):
    hospital_name=models.CharField(max_length=200)
    hospital_id=models.CharField(max_length=50)
    def __str__(self):
        return self.hospital_name
class reports(models.Model):
    disease=models.CharField(max_length=500)
    #pdff=models.ImageField(null=True,blank=True,upload_to='images/')
    adno=models.CharField(max_length=12)
    dat=models.CharField(max_length=10,default='00000000')
    diag = models.CharField(max_length=500,default='0000000')
    prec = models.CharField(max_length=1000,default='0000000000000')
    rem = models.CharField(max_length=1000,default='000000000')
    urlf=models.CharField(max_length=1000,default="XXXXXXX")
class pad(models.Model):
    passwd=models.CharField(max_length=50)
    adno=models.CharField(max_length=12)
    def __str__(self):
        return self.adno
class tempreports(models.Model):
    disease:str
    #pdff=models.ImageField(null=True,blank=True,upload_to='images/')
    adno:str
    dat:str
    diag:str
    prec:str
    rem:str
    urlf:str


