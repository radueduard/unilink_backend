import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Serializers.schedule import ScheduleSerializer

from ..Models.grupa import Grupa
from ..Models.semigrupa import Semigrupa
from ..Models.serie import Serie


@api_view(['GET'])
def get(request, pk):
    try:
        uuid.UUID(pk)
    except ValueError:
        return Response("No such UUID")

    semigrupa = None
    if Semigrupa.objects.filter(id=pk):
        semigrupa = Semigrupa.objects.get(id=pk)
    else:
        return Response("No such semigrupa")

    grupa = Grupa.objects.get(id=semigrupa.grupa.id)
    serie = Serie.objects.get(id=grupa.serie.id)

    cursuri = serie.cursuri.all()
    seminare = grupa.seminare.all()
    laboratoare = semigrupa.laboratoare.all()

    schedules = []
    for curs in cursuri:
        s = curs.schedules.all()
        for sc in s:
            schedules = schedules + [sc]
    for seminar in seminare:
        s = seminar.schedules.all()
        for sc in s:
            schedules = schedules + [sc]
    for lab in laboratoare:
        s = lab.schedules.all()
        for sc in s:
            schedules = schedules + [sc]

    return Response(ScheduleSerializer(schedules, many=True).data)
