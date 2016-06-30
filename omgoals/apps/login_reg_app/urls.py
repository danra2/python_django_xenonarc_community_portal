from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^validate$', views.validation, name='validation'),
    url(r'^dashboard$', views.dash, name='dashboard'),
]
