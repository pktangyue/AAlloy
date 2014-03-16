from django.contrib import admin
from clip.models import Window, Material, Product, ProductTrim, ProductName

class ProductInline(admin.StackedInline):
    model = Product
    extra = 0

class WindowAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

class ProductTrimInline(admin.StackedInline):
    model = ProductTrim
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    inlines = [ProductTrimInline]

admin.site.register(Window, WindowAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Product)
admin.site.register(ProductName)
admin.site.register(ProductTrim)
