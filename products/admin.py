from django.contrib import admin

# Register your models here.
from products.models import *

admin.site.register([Product, ProductImage, Size, Units])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
