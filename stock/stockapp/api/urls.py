from django.urls import path
# from rest_framework import routers

from .views import StockList, StockDetail

# router = routers.DefaultRouter()
# router.register(r'api', StockViews)
app_name = 'stock-api'

urlpatterns = [
    # path('', include(router.urls)),
    path('api/', StockList.as_view(), name='stock-list'),
    path('api/<pk>/', StockDetail.as_view(), name="stock-detail"),
]
