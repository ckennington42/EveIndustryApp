from django.contrib import admin

# Register your models here.
from apps.app.models import InvType, MarketGroup


class InvTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'group_id', 'name', 'market_group_name')
admin.site.register(InvType, InvTypeAdmin)

class MarketGroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'parent_id', 'name')
admin.site.register(MarketGroup, MarketGroupAdmin)
