from django.contrib import admin

from products.models import Category, Product


admin.site.site_header = "Demo SQA Admin"
admin.site.site_title = "Demo SQA Admin Portal"
admin.site.index_title = "Welcome to Demo SQA Testing Portal"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['name',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category__name', 'price', 'stock', 'created_at', 'updated_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'category__name', 'stock']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
