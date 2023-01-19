from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..Models.customSchedule import CustomInclusion
from rest_framework.authtoken.models import Token

from ..Models.student import Student
from ..Serializers.customSchedule import InclusionSerializer


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def post(request):
    data = {
        'student': Token.objects.get(key=request.auth.key).user_id,
        'schedule': request.data['id']
    }
    serializer = InclusionSerializer(data=data, many=False)
    if serializer.is_valid():
        data = {
            'mesaj': 'This schedule will be included',
            'schedule': serializer.validated_data['schedule']
        }
        serializer.save()
        return Response(data)
    else:
        return Response(serializer.errors)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated, ])
def delete(request, pk):
    user_id = Token.objects.get(key=request.auth.key).user_id
    inclusion = CustomInclusion.objects.get(id=pk)
    if inclusion.student == user_id:
        data = {
            'mesaj': 'Your inclusion was successfully deleted',
            'schedule': inclusion.schedule.__str__()
        }
        CustomInclusion.objects.delete(id=inclusion.id)
        return Response(data)
    else:
        return Response({'mesaj': 'It is not yours to delete'})


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def get(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    student = Student.objects.get(id=user_id)
    inclusions = CustomInclusion.objects.filter(student=student.id)
    serializer = InclusionSerializer(inclusions, many=True, read_only=True)
    return Response(serializer.data)
