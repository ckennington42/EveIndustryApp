from django.contrib import admin
from .models import *

# Register your models here.


class AssetAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity')
admin.site.register(Asset, AssetAdmin)