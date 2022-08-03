from django.contrib import admin
from products.models import HierarchicalTag, Product, ProductCategory
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory



class HierarchicalTagAdmin(TreeAdmin):
    form = movenodeform_factory(HierarchicalTag)


class CategoryInline(admin.TabularInline):
    model = ProductCategory
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(HierarchicalTag, HierarchicalTagAdmin)


# Register your models here.
