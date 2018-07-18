from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'checkout$', views.checkoutdone),
    url(r'checkoutprocess$', views.processbuy),
    url(r'addproduct$', views.addproduct),
    url(r'addprocess$', views.addprocess)
] 