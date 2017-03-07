from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from .views import BrandListView, BrandDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$', BrandListView.as_view(), name='brands'),
    url(r'^(?P<slug>[\w-]+)/$', BrandDetailView.as_view(), name='brand_detail'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]