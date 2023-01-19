from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..Models.grupa import Grupa
from ..Models.materie import Curs
from ..Models.semigrupa import Semigrupa
from ..Models.serie import Serie
from ..Models.singletimeevent import Tema, Examen
from ..Models.student import Student
from ..Serializers.singletimeevent import TemaSerializer, ExamenSerializer


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def get_teme(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    user = Student.objects.get(id=user_id)

    semigrupa = Semigrupa.objects.get(id=user.semigrupa.id)
    grupa = Grupa.objects.get(id=semigrupa.grupa.id)
    serie = Serie.objects.get(id=grupa.serie.id)

    cursuri = Curs.objects.filter(serie=serie.id)

    response = []
    for curs in cursuri:
        teme = Tema.objects.filter(curs=curs.id)
        for tema in teme:
            response = response + [tema]

    response = TemaSerializer(response, many=True, read_only=True)

    return Response(response.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def post_tema(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    curs = Curs.objects.get(id=request.data['curs'])
    if curs.profesor.__str__() == user_id:
        serializer = TemaSerializer(request.data)
        if serializer.is_valid():
            data = {
                'mesaj': 'Tema a fost postata cu succes',
                'tema': serializer.validated_data
            }
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)
    else:
        return Response({'mesaj': 'Nu poti posta o tema pentru acest curs'})


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated, ])
def delete_tema(request, pk):
    user_id = Token.objects.get(key=request.auth.key).user_id
    tema = Tema.objects.get(id=pk)
    curs = Curs.objects.get(id=tema.curs)
    if user_id == curs.profesor:
        Tema.objects.delete(id=pk)
        return Response({'mesaj': 'Tema a fost stearsa cu succes'})
    return Response({'mesaj': 'Nu poti sterge aceasta tema'})


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def get_examene(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    user = Student.objects.get(id=user_id)

    semigrupa = Semigrupa.objects.get(id=user.semigrupa.id)
    grupa = Grupa.objects.get(id=semigrupa.grupa.id)
    serie = Serie.objects.get(id=grupa.serie.id)

    cursuri = Curs.objects.filter(serie=serie.id)

    response = []
    for curs in cursuri:
        examene = Examen.objects.filter(curs=curs.id)
        for examen in examene:
            response = response + [examen]

    response = ExamenSerializer(response, many=True, read_only=True)

    return Response(response.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def post_examen(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    curs = Curs.objects.get(id=request.data['curs'])
    if curs.profesor.__str__() == user_id:
        serializer = ExamenSerializer(request.data)
        if serializer.is_valid():
            data = {
                'mesaj': 'Examenul a fost planificat cu succes',
                'examen': serializer.validated_data
            }
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)
    else:
        return Response({'mesaj': 'Nu poti planifica un examen pentru acest curs'})


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated, ])
def delete_examen(request, pk):
    user_id = Token.objects.get(key=request.auth.key).user_id
    examen = Examen.objects.get(id=pk)
    curs = Curs.objects.get(id=examen.curs)
    if user_id == curs.profesor:
        Examen.objects.delete(id=pk)
        return Response({'mesaj': 'Examenul a fost sters cu succes'})
    return Response({'mesaj': 'Nu poti sterge examenul'})