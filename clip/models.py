from django.db import models

class Window(models.Model):
#    x = models.DecimalField(default=0)
#    y = models.DecimalField(default=0)
#    m = models.DecimalField(default=0)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    window = models.ForeignKey(Window)
    name = models.CharField(max_length=50)
    num = models.IntegerField(default=0)
    formula = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class ProductTrim(models.Model):
    window = models.ForeignKey(Window)
    material = models.ForeignKey(Material)
    product = models.ForeignKey(Product)
    trim_length = models.DecimalField(default=0, max_digits=10, decimal_places=3)
