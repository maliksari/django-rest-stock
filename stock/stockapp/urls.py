from django.urls import path, include

app_name = 'stockapp'

urlpatterns = [
    path('', include("stockapp.api.urls")),
]
