from django.contrib import admin
from clip.models import *

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class WindowAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

class ProductTrimInline(admin.TabularInline):
    model = ProductTrim
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    inlines = [ProductTrimInline]

class RecordProductInline(admin.TabularInline):
    model = RecordProduct
    extra = 0

class RecordWindowInline(admin.TabularInline):
    model = RecordWindow
    extra = 0

class RecordAdmin(admin.ModelAdmin):
    inlines = [RecordProductInline, RecordWindowInline]

admin.site.register(Window, WindowAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Product)
admin.site.register(ProductName)
admin.site.register(ProductTrim)
admin.site.register(Record, RecordAdmin)
admin.site.register(RecordWindow)
admin.site.register(RecordProduct)
