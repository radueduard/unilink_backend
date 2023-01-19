from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Models.an import An
from ..Serializers.facultate import *


@api_view(['GET'])
def get(request, pk):
    an = An.objects.get(id=pk)
    serializer = AnSerializer(an, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    ani = An.objects.all()
    serializer = AnSerializer(ani, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_from_facultate(request, facultate):
    ani = An.objects.filter(facultate=facultate)
    serializer = AnSerializer(ani, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    An.objects.get(id=pk).delete()
    return Response({'mesaj': 'Deleted'})


@api_view(['DELETE'])
def deletes(request):
    An.objects.all().delete()
    return Response({'mesaj': 'Deleted all'})


@api_view(['POST'])
def post(request):
    serializer = AnSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)