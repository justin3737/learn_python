# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='https://imgur.com/TQTfGiA')  #說明此規格的網址

    def __str__(self):
        return self.name


class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, default='超值Xpro3')
    description = models.TextField(default='暫無說明')
    year = models.PositiveIntegerField(default=2020)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname


class PPhoto(models.Model):
    pmodel = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='產品照片')
    url = models.URLField(default='https://imgur.com/TQTfGiA')  #儲存照片的位置

    def __str__(self):
        return self.description