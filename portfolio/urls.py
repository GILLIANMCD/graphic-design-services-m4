from django.conf.urls import url, include
from .views import all_portfolios


urlpatterns = [
    url(r'^$', all_portfolios, name='portfolio')
    ]