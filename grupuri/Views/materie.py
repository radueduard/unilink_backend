from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..Serializers.materie import *
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def get(request, pk):
    facultate = Materie.objects.get(id=pk)
    serializer = MaterieSerializer(facultate, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def deletes(request):
    print(request.user)
    Materie.objects.all().delete()
    return Response("Deleted")


@api_view(['GET'])
def gets(request):
    materii = Materie.objects.all()
    serializer = MaterieSerializer(materii, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post(request):
    serializer = MaterieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    Materie.objects.get(id=pk).delete()
    return Response("Deleted")
