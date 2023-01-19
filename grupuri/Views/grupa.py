from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Models.grupa import Grupa
from ..Serializers.grupa import GrupaSerializer


@api_view(['GET'])
def get(request, pk):
    grupa = Grupa.objects.get(id=pk)
    serializer = GrupaSerializer(grupa, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    grupe = Grupa.objects.all()
    serializer = GrupaSerializer(grupe, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_from_serie(request, serie):
    grupe = Grupa.objects.filter(serie=serie)
    serializer = GrupaSerializer(grupe, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    Grupa.objects.get(id=pk).delete()
    return Response("Deleted")


@api_view(['DELETE'])
def deletes(request):
    Grupa.objects.all().delete()
    return Response("Deleted")


@api_view(['POST'])
def post(request):
    serializer = GrupaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
