from django.db.models import QuerySet
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..Models.grupa import Grupa
from ..Models.materie import Curs, Seminar, Laborator
from ..Models.semigrupa import Semigrupa
from ..Models.serie import Serie
from ..Models.student import Student
from ..Serializers.schedule import *


@api_view(['GET'])
def get(request, pk):
    schedule = Schedule.objects.get(id=pk)
    serializer = ScheduleSerializer(schedule, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def gets(request, materia_id):
    schedules = Schedule.objects.filter(materie=materia_id)
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)


#########################################################################
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_personal(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    user = Student.objects.get(id=user_id)

    semigrupa = Semigrupa.objects.get(id=user.semigrupa.id)
    grupa = Grupa.objects.get(id=semigrupa.grupa.id)
    serie = Serie.objects.get(id=grupa.serie.id)

    cursuri = Curs.objects.filter(serie=serie.id)
    seminare = Seminar.objects.filter(grupa=grupa.id)
    laboratoare = Laborator.objects.filter(semigrupa=semigrupa.id)

    curs_sch = []
    for curs in cursuri:
        schedules = ScheduleC.objects.filter(curs=curs)
        for schedule in schedules:
            curs_sch = curs_sch + [schedule]

    sem_sch = []
    for seminar in seminare:
        schedules = ScheduleS.objects.filter(seminar=seminar)
        for schedule in schedules:
            sem_sch = sem_sch + [schedule]

    lab_sch = []
    for laborator in laboratoare:
        schedules = ScheduleL.objects.filter(laborator=laborator)
        for schedule in schedules:
            lab_sch = lab_sch + [schedule]

    cursuri = ScheduleCSerializer(curs_sch, many=True)
    seminare = ScheduleSSerializer(sem_sch, many=True)
    laboratoare = ScheduleLSerializer(lab_sch, many=True)

    data = {
        'cursuri': cursuri.data,
        'seminare': seminare.data,
        'laboratoare': laboratoare.data
    }

    return Response(data=data)

#########################################################################


@api_view(['GET'])
def get_from_semigrupa(request, id):
    semigrupa = Semigrupa.objects.get(id=id)
    grupa = Grupa.objects.get(id=semigrupa.grupa.id)
    serie = Serie.objects.get(id=grupa.serie.id)

    cursuri = Curs.objects.filter(serie=serie.id)
    seminare = Seminar.objects.filter(grupa=grupa.id)
    laboratoare = Laborator.objects.filter(semigrupa=semigrupa.id)

    curs_sch = []
    for curs in cursuri:
        schedules = ScheduleC.objects.filter(curs=curs)
        for schedule in schedules:
            curs_sch = curs_sch + [schedule]

    sem_sch = []
    for seminar in seminare:
        schedules = ScheduleS.objects.filter(seminar=seminar)
        for schedule in schedules:
            sem_sch = sem_sch + [schedule]

    lab_sch = []
    for laborator in laboratoare:
        schedules = ScheduleL.objects.filter(laborator=laborator)
        for schedule in schedules:
            lab_sch = lab_sch + [schedule]

    cursuri = ScheduleCSerializer(curs_sch, many=True)
    seminare = ScheduleSSerializer(sem_sch, many=True)
    laboratoare = ScheduleLSerializer(lab_sch, many=True)

    data = {
        'cursuri': cursuri.data,
        'seminare': seminare.data,
        'laboratoare': laboratoare.data
    }

    return Response(data=data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_curs(request):
    serializer = ScheduleCSerializer(data=request.data)
    if serializer.is_valid():
        curs = Curs.objects.get(id=serializer.validated_data['curs'].id)
        user = Token.objects.get(key=request.auth.key).user_id

        if user != curs.profesor.id:
            return Response({{'mesaj': 'Nu poti creea un schedule pentru acest curs'}})
        schedule = serializer.save()
        data = {
            'curs': CursSerializer(curs).data,
            'week': schedule.week,
            'day': schedule.day,
            'sala': schedule.sala.id,
            'startingHour': schedule.startingHour
        }
        return Response(data)
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_seminar(request):
    serializer = ScheduleSSerializer(data=request.data)
    if serializer.is_valid():
        seminar = Seminar.objects.get(id=serializer.validated_data['seminar'].id)
        user = Token.objects.get(key=request.auth.key).user_id

        if user != seminar.seminarist.id:
            return Response({{'mesaj': 'Nu poti creea un schedule pentru acest seminar'}})
        schedule = serializer.save()
        data = {
            'seminar': SeminarSerializer(seminar).data,
            'week': schedule.week,
            'day': schedule.day,
            'sala': schedule.sala.id,
            'startingHour': schedule.startingHour
        }
        return Response(data)
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def add_laborator(request):
    serializer = ScheduleLSerializer(data=request.data)
    if serializer.is_valid():
        laborator = Laborator.objects.get(id=serializer.validated_data['laborator'].id)
        user = Token.objects.get(key=request.auth.key).user_id

        if user != laborator.asistent.id:
            return Response({{'mesaj': 'Nu poti creea un schedule pentru acest laborator'}})
        schedule = serializer.save()
        data = {
            'laborator': LaboratorSerializer(laborator).data,
            'week': schedule.week,
            'day': schedule.day,
            'sala': schedule.sala.id,
            'startingHour': schedule.startingHour
        }
        return Response(data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete(request, pk):
    Schedule.objects.get(id=pk).delete()
    return Response("Deleted")


@api_view(['DELETE'])
def deletes(request):
    Schedule.objects.all().delete()
    return Response("Deleted")
