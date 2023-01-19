from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Models.materie import Curs
from ..Serializers.materie import CursSerializer


@api_view(['GET'])
def get(request, pk):
    curs = Curs.objects.get(id=pk)
    serializer = CursSerializer(curs, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    cursuri = Curs.objects.all()
    serializer = CursSerializer(cursuri, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deletes(request):
    Curs.objects.all().delete()
    return Response("Deleted")


@api_view(['DELETE'])
def delete(request, pk):
    Curs.objects.get(id=pk).delete()
    return Response("Deleted")


@api_view(['POST'])
def post(request):
    serializer = CursSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def put(request, pk):
    serializer = CursSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
