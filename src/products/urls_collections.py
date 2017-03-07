from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from .views import CollectionListView, CollectionDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$', CollectionListView.as_view(), name='collections'),
    url(r'^(?P<slug>[\w-]+)/$', CollectionDetailView.as_view(), name='collection_detail'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]