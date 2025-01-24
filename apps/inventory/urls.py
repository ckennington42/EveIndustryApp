from django.urls import include, path

from . import views


urlpatterns = [
    path('inventory/', views.inventory_view, name='inventory'),
    path('inventory/refresh/', views.refresh_inventory, name='refesh_assets'),
    path('inventory/clear/', views.clear_inventory, name='clear_assets'),
]