from django.conf.urls import url
from .views import portfolio


urlpatterns = [
    url(r'^$', portfolio, name='portfolio')
    ]