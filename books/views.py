from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
# Create your views here.

class GetInfo(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs): 
        # serializer_class = BookSerializer
        # Saco mi elemento de bd
        info = Book.objects.get(id = kwargs['pk'])
        # Convierto
        test = BookSerializer(info)
        print(test.data)
        print(info)
        return Response(test.data)
    
