from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@swagger_auto_schema(method="GET",
                     operation_description="Test Endpoint for pinging", responses={200: 'ping'})
@api_view(["GET"])
def ping(request):
    message = {"reply": "ping"}
    return Response(message)
