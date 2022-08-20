from django.shortcuts import render, HttpResponse
from .models import kegiatan
from .serializers import SerializerKegiatan
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins


class KegiatanList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = kegiatan.objects.all()
    serializer_class = SerializerKegiatan

    def get(self, request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)        


class KegiatanDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = kegiatan.objects.all()
    serializer_class = SerializerKegiatan
    lookup_field ='id'

    def get(self, request, id):
        return self.retrieve(request, id=id)
    
    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self,request,id):
        return self.destroy(request, id=id)
    


'''

@api_view(['GET','POST'])
def kegiatan_list(request):
    #get all kegiatan list
    if request.method == 'GET':
        Kegiatan = kegiatan.objects.all()
        serializer = SerializerKegiatan(Kegiatan, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SerializerKegiatan(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def kegiatan_details(request, pk):
    try:
        Kegiatan = kegiatan.objects.get(pk=pk)

    except kegiatan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = SerializerKegiatan(Kegiatan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SerializerKegiatan(Kegiatan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Kegiatan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

'''

    
        
