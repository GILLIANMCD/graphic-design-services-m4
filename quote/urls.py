from django.conf.urls import url
from .views import get_quote

urlpatterns = [
    url(r'^$', get_quote, name='get_quote')
    ]