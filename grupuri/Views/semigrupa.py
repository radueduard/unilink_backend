from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Models.semigrupa import Semigrupa
from ..Serializers.semigrupa import SemigrupaSerializer


@api_view(['GET'])
def get(request, pk):
    semigrupa = Semigrupa.objects.get(id=pk)
    serializer = SemigrupaSerializer(semigrupa, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    semigrupe = Semigrupa.objects.all()
    serializer = SemigrupaSerializer(semigrupe, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_from_grupa(request, grupa):
    semigrupe = Semigrupa.objects.filter(grupa=grupa)
    serializer = SemigrupaSerializer(semigrupe, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    Semigrupa.objects.get(id=pk).delete()
    return Response("Deleted")


@api_view(['DELETE'])
def deletes(request):
    Semigrupa.objects.all().delete()
    return Response("Deleted")


@api_view(['POST'])
def post(request):
    serializer = SemigrupaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
