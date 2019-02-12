from django.conf.urls import patterns, url, include
from rest_framework import routers

from product_app.views import ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, base_name='product')
router.register(r'category', CategoryViewSet, base_name='category')

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )
