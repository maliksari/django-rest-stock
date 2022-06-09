from django.urls import path, include

app_name = 'stockapp'

urlpatterns = [
    path('stock/', include("stockapp.api.urls")),
]
