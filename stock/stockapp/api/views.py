from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from ..models import Stock
from .serializer import StockSerializer


# class StockViews(ModelViewSet):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#     permission_classes = [IsAuthenticated]


class StockList(APIView):

    def get(self, request):
        queryset = Stock.objects.all()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDetail(APIView):
    def get(self, request, pk, format=None):
        queryset = get_object_or_404(Stock.objects.all(), pk=pk)
        serializer = StockSerializer(queryset)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = get_object_or_404(Stock.objects.all(), pk=pk)
        serializer = StockSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = get_object_or_404(Stock.objects.all(), pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
