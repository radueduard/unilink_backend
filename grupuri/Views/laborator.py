from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Models.materie import Laborator
from ..Serializers.materie import LaboratorSerializer


@api_view(['GET'])
def get(request, pk):
    laborator = Laborator.objects.get(id=pk)
    serializer = LaboratorSerializer(laborator, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    laboratoare = Laborator.objects.all()
    serializer = LaboratorSerializer(laboratoare, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deletes(request):
    Laborator.objects.all().delete()
    return Response("Deleted")


@api_view(['DELETE'])
def delete(request, pk):
    Laborator.objects.get(id=pk).delete()
    return Response("Deleted")


@api_view(['POST'])
def post(request):
    serializer = LaboratorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def put(request, pk):
    serializer = LaboratorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
