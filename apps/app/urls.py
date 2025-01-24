from django.urls import include, path
from .views.index import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
]