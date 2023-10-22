from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q
from .models import MainObject
from .serializers import MainObjectSerializer
# Create your views here.

@swagger_auto_schema(method="GET",
                     operation_description="Test Endpoint for pinging", responses={200: 'ping'})
@api_view(["GET"])
def ping(request):
    message = {"reply": "ping"}
    return Response(message)


class MainObjectSearch(generics.ListAPIView):
    serializer_class = MainObjectSerializer
    queryset = MainObject.objects.all()

    def get(self, request, *args, **kwargs):
        search_term = self.request.query_params.get('query', '')
        if len(search_term) < 1:
            return Response([], status=status.HTTP_200_OK)
        keywords = search_term.split()
        q_objects = []

        for keyword in keywords:
            q_objects.append(Q(name__icontains=keyword) | Q(postcode__icontains=keyword))
        query = q_objects.pop()
        for item in q_objects:
            query |= item
        queryset = self.queryset.filter(query).distinct().order_by('-name')

        serializer = MainObjectSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MainObjectList(generics.ListCreateAPIView):
    queryset = MainObject.objects.all()
    serializer_class = MainObjectSerializer

class MainObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainObject.objects.all()
    serializer_class = MainObjectSerializer