from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()


class UserCreateView(generics.GenericAPIView):
    """ A QuizzesView for handling various Quiz related methods """
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Acount created"}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)