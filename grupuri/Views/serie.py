from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Models.serie import Serie
from ..Serializers.serie import SerieSerializer


@api_view(['GET'])
def get(request, pk):
    serie = Serie.objects.get(id=pk)
    serializer = SerieSerializer(serie, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    serii = Serie.objects.all()
    serializer = SerieSerializer(serii, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_from_an(request, an):
    serii = Serie.objects.filter(an=an)
    serializer = SerieSerializer(serii, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    Serie.objects.get(id=pk).delete()
    return Response("Deleted")


@api_view(['DELETE'])
def deletes(request):
    Serie.objects.all().delete()
    return Response("Deleted")


@api_view(['POST'])
def post(request):
    serializer = SerieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
