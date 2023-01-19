from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from ..Models.student import Student
from ..Serializers.semigrupa import SemigrupaSerializer
from ..Serializers.student import StudentRegisterSerializer, StudentAllInfoSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def register(request):
    if request.method == 'POST':
        serializer = StudentRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            student = serializer.save()
            data['response'] = 'am creat studentu\''
            data['email'] = student.email
            data['username'] = student.username
            data['semigrupa'] = SemigrupaSerializer(student.semigrupa).data
            token = Token.objects.get(user=student).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def getAccountInfo(request):
    student = Token.objects.get(key=request.auth.key).user_id
    try:
        student = Student.objects.get(id=student)
        data = StudentAllInfoSerializer(student)
        return Response(data=data.data)
    except():
        return Response(0)
    return Response(0)
