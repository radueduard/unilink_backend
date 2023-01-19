from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..Models.customSchedule import CustomExclusion
from rest_framework.authtoken.models import Token

from ..Models.student import Student
from ..Serializers.customSchedule import ExclusionSerializer


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def post(request):
    data = {
        'student': Token.objects.get(key=request.auth.key).user_id,
        'schedule': request.data['id']
    }
    serializer = ExclusionSerializer(data=data, many=False)
    if serializer.is_valid():
        data = {
            'mesaj': 'This schedule will be excluded',
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
    exclusion = CustomExclusion.objects.get(id=pk)
    if exclusion.student == user_id:
        data = {
            'mesaj': 'Your exclusion was successfully deleted',
            'schedule': exclusion.schedule.__str__()
        }
        CustomExclusion.objects.delete(id=exclusion.id)
        return Response(data)
    else:
        return Response({'mesaj':'It is not yours to delete'})


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def get(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    student = Student.objects.get(id=user_id)
    exclusions = CustomExclusion.objects.filter(student=student.id)
    serializer = ExclusionSerializer(exclusions, many=True, read_only=True)
    return Response(serializer.data)