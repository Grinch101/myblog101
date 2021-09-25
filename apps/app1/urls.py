from django.urls.conf import include, path
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('getall/', views.get_all)
]