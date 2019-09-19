"""django_auth URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from accounts import urls as accounts_urls
from products import urls as urls_products
from cart import urls as urls_cart
from contact import urls as urls_contact
from quote import urls as urls_quote
from portfolio import urls as urls_portfolio
from posts import urls as urls_post
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT
from .views import home
from .views import about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="index"),
    url(r'about', about, name="about"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^posts/', include(urls_post)),
    url(r'^products/', include(urls_products)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^cart/', include(urls_cart)),
    url(r'^contact/', include(urls_contact)),
    url(r'^quote/', include(urls_quote)),
    url(r'^portfolio/', include(urls_portfolio)),
    url(r'^search/', include(urls_search)),
   url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]