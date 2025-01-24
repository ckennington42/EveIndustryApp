from django.urls import include, path

from . import views


urlpatterns = [
    path('estimator/', views.inventory_view, name='estimator'),
]