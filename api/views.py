from django.shortcuts import render
from django.views.generic.list import ListView

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BasicSerializer, MarketSerializer

from .models import Etherscan, Coinmarketcap


class CoinmarketcapListView(ListView):

    model = Coinmarketcap
    # template_name = "api/xtrd_parse.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Coinmarketcap.objects.last()
        print(context['data'])
        return context

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of API.
    """
    return Response({
        'basic': reverse('basic-metrics', request=request),
        'markets': reverse('markets-info', request=request)})


class BasicView(APIView):
    """
    Get basic metrics for XTRD token 
    """
    serializer_class = BasicSerializer

    @staticmethod
    def get(request):
        data = {
            "supply": 952457688.00,
            "price": {
                "usd": 0.01,
                "eth": 0.0001
            },
            "volume": 10000.00
        }
        return Response(data, status=status.HTTP_200_OK)


class MarketsView(APIView):
    """
    Get information about markets where the token is trading and corresponding metrics like price and volume. 
    """
    serializer_class = MarketSerializer

    @staticmethod
    def get(request):
        data = [{
            "name": "Exchange_1",
            "volume": 3000,
            "share": 50.00
            },
            {
                "name": "Exchange_2",
                "volume": 2000,
                "share": 30.00
            },
            {
                "name": "Exchange_3",
                "volume": 1000,
                "share": 20.00
            }]
        return Response(data, status=status.HTTP_200_OK)