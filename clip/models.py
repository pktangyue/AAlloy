from django.db import models

class Window(models.Model):
    name = models.CharField(max_length=50)
    need_m = models.BooleanField(default=False)
    need_z = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class ProductName(models.Model):
    name = models.CharField(max_length=50)
    formula = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name  + "(" + self.formula + ")"

class Product(models.Model):
    window = models.ForeignKey(Window)
    product_name = models.ForeignKey(ProductName)
    num = models.IntegerField(default=0)

    def __unicode__(self):
        return self.window.__unicode__() + " : " + self.product_name.__unicode__()

class ProductTrim(models.Model):
    material = models.ForeignKey(Material)
    product = models.ForeignKey(Product)
    trim_length = models.DecimalField(default=0, max_digits=10, decimal_places=3)

    def __unicode__(self):
        return self.material.__unicode__() + " : " + self.product.__unicode__()
