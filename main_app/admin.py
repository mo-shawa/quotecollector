from django.contrib import admin
from .models import Category, Quote, Fan, Category
# Register your models here.

admin.site.register((Category))
admin.site.register((Quote))
admin.site.register((Fan))