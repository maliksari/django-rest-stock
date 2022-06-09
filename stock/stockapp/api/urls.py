from django.urls import path
# from rest_framework import routers

from .views import StockList, StockDetail

# router = routers.DefaultRouter()
# router.register(r'api', StockViews)

urlpatterns = [
    # path('', include(router.urls)),
    path('', StockList.as_view()),
    path('<pk>/', StockDetail.as_view()),
]
