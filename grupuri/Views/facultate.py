from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..Serializers.facultate import *


@api_view(['GET'])
def get(request, pk):
    facultate = Facultate.objects.get(id=pk)
    serializer = FacultateSerializer(facultate, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    facultati = Facultate.objects.all()
    serializer = FacultateSerializer(facultati, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    Facultate.objects.get(id=pk).delete()
    return Response({'mesaj': 'Deleted'})


@api_view(['DELETE'])
def deletes(request):
    Facultate.objects.all().delete()
    return Response({'mesaj': 'Deleted all'})


@api_view(['POST'])
def post(request):
    serializer = FacultateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


