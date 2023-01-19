import datetime

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from ..Models.grupa import Grupa
from ..Models.materie import Curs, Laborator, Seminar
from ..Models.semigrupa import Semigrupa
from ..Models.serie import Serie
from ..Models.student import Student
from ..Models.notification import NotificationLab, NotificationSeminar, NotificationCourse, NotificationSchedule
from ..Serializers.notification import NotificationCourseSerializer, \
    NotificationSeminarSerializer, NotificationLabSerializer, NotificationCourseSerializerPOST


def is_delete(created):
    notif_created = created
    time_now = datetime.datetime.now()
    dif = time_now - notif_created.replace(tzinfo=None)
    if dif > datetime.timedelta(days=7):
        return True
    return False


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def get_notifications(request):
    for notification in NotificationSchedule.objects.all():
        if is_delete(notification.created):
            NotificationSchedule.objects.filter(id=notification.id).delete()
    user_id = Token.objects.get(key=request.auth.key).user_id

    user = Student.objects.get(id=user_id)
    semigrupa = Semigrupa.objects.get(id=user.semigrupa.id)
    grupa = Grupa.objects.get(id=semigrupa.grupa.id)
    serie = Serie.objects.get(id=grupa.serie.id)

    cursuri = Curs.objects.filter(serie=serie.id)
    seminarii = Seminar.objects.filter(grupa=grupa.id)
    laboratoare = Laborator.objects.filter(semigrupa=semigrupa.id)

    notification_course_list = []
    for curs in cursuri:
        notifications = NotificationCourse.objects.filter(sender=curs.id)
        for notification in notifications:
            notification_course_list = notification_course_list + [notification]

    notification_seminar_list = []
    for seminar in seminarii:
        notifications = NotificationSeminar.objects.filter(sender=seminar.id)
        for notification in notifications:
            notification_seminar_list = notification_seminar_list + [notification]

    notification_lab_list = []
    for laborator in laboratoare:
        notifications = NotificationLab.objects.filter(sender=laborator.id)
        for notification in notifications:
            notification_lab_list = notification_lab_list + [notification]

    course_notifications = NotificationCourseSerializer(notification_course_list, many=True)
    seminar_notifications = NotificationSeminarSerializer(notification_seminar_list, many=True)
    lab_notifications = NotificationLabSerializer(notification_lab_list, many=True)

    data = {
        'cursuri': course_notifications.data,
        'seminare': seminar_notifications.data,
        'laboratoare': lab_notifications.data
    }

    return Response(data=data)


@api_view(['POST', ])
def create_notification_course(request):
    for notification in NotificationSchedule.objects.all():
        if is_delete(notification.created):
            NotificationSchedule.objects.filter(id=notification.id).delete()
    data = {
        'sender': request.data['sender'],
        'mesaj': request.data['mesaj'],
    }
    notification = NotificationCourseSerializerPOST(data=data)
    if notification.is_valid():
        notification.save()
        return Response(notification.data, status=status.HTTP_201_CREATED)
    return Response(notification.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def create_notification_seminar(request):
    for notification in NotificationSchedule.objects.all():
        if is_delete(notification.created):
            NotificationSchedule.objects.filter(id=notification.id).delete()
    data = {
        'sender': request.data['sender'],
        'mesaj': request.data['mesaj'],
    }
    notification = NotificationSeminarSerializer(data=data)
    if notification.is_valid():
        notification.save()
        return Response(notification.data, status=status.HTTP_201_CREATED)
    return Response(notification.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def create_notification_lab(request):
    for notification in NotificationSchedule.objects.all():
        if is_delete(notification.created):
            NotificationSchedule.objects.filter(id=notification.id).delete()
    data = {
        'sender': request.data['sender'],
        'mesaj': request.data['mesaj'],
    }
    notification = NotificationLabSerializer(data=data)
    if notification.is_valid():
        notification.save()
        return Response(notification.data, status=status.HTTP_201_CREATED)
    return Response(notification.errors, status=status.HTTP_400_BAD_REQUEST)
