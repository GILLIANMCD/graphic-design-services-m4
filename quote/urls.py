from django.conf.urls import url
from .views import quote

urlpatterns = [
    url(r'^$', quote, name='quote')
    ]