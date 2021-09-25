from django.urls.conf import include, path
from . import views
from django.urls import path


urlpatterns = [
    path('test/', views.index),
    path('', views.get_all)
]