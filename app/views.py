from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters
from .models import MainObject
from .serializers import MainObjectSerializer

# Create your views here.

@swagger_auto_schema(method="GET",
                     operation_description="Test Endpoint for pinging", responses={200: 'ping'})
@api_view(["GET"])
def ping(request):
    message = {"reply": "ping"}
    return Response(message)


class MainObjectListView(generics.ListCreateAPIView):
    queryset = MainObject.objects.all()
    serializer_class = MainObjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','description']


