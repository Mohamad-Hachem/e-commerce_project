from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header = "Mohamad's E-commerce Site"
admin.site.site_title = "Mohamad's E-commerce"
admin.site.index_title = "Manage Mohamad's E-commerce "

admin.site.register(Products)
admin.site.register(Order)
