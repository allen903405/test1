#vim: set fileencoding=utf-8 :

from django.db import models

# Create your models here.

class Company(models.Model):
    full_name = models.CharField(u'公司全称' ,max_length=30)
    address = models.CharField(u'地址', max_length=50)
    tel = models.CharField(u'电话', max_length=15,blank=True)

    def __unicode__(self):
        return  '%s %s %s' % (self.full_name,self.address,self.tel)

class Product(models.Model):
    product_name = models.CharField(u'产品名称', max_length=30)
    price = models.FloatField(u'价格')
    stock = models.IntegerField(u'库存', max_length=5)
    company = models.ForeignKey(Company)
    create_date = models.DateField(u'生产日期')

    def __unicode__(self):
        return self.product_name
    #设置一些与特定模型相关的选项
    class Meta:
        ordering = ['create_date']
