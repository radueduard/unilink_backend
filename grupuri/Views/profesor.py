from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..Serializers.profesor import ProfesorRegisterSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def register(request):
    if request.method == 'POST':
        serializer = ProfesorRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            profesor = serializer.save()
            data['response'] = 'am creat profu\''
            data['email'] = profesor.email
            data['username'] = profesor.username
            data['tip'] = profesor.tip
            token = Token.objects.get(user=profesor).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
