from django.shortcuts import render
from .models import Recipe

from rest_framework import viewsets
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class RecipeViewSet(viewsets.ViewSet):
    def list(self,request):
        recipe=Recipe.objects.all()
        serializer=RecipeSerializer(recipe,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            recipe=Recipe.objects.get(id=id)
            serializer=RecipeSerializer(recipe)
            return Response(serializer.data)
        
    def create(self,request):
        serializer=RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        id=pk
        recipe=Recipe.objects.get(pk=id)
        serializer=RecipeSerializer(recipe,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def distroy(self,request,pk=None):
        id=pk
        recipe=Recipe.objects.get(pk=id)
        recipe.delete()
        return Response({'msg':'Data Deleted'})
    

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
  
    
                