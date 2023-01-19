from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..Models.materie import Seminar
from ..Serializers.materie import SeminarSerializer

@api_view(['GET'])
def get(request, pk):
    seminar = Seminar.objects.get(id=pk)
    serializer = SeminarSerializer(seminar, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request):
    seminare = Seminar.objects.all()
    serializer = SeminarSerializer(seminare, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deletes(request):
    Seminar.objects.all().delete()
    return Response("Deleted")


@api_view(['DELETE'])
def delete(request, pk):
    Seminar.objects.get(id=pk).delete()
    return Response("Deleted")


@api_view(['POST'])
def post(request):
    serializer = SeminarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def put(request, pk):
    serializer = SeminarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)