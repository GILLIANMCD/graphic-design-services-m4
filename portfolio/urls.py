from django.conf.urls import url, include
from .views import portfolio


urlpatterns = [
    url(r'^$', portfolio, name='portfolio')
    ]