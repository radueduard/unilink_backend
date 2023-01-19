from django.urls import path
from .Views import schedule, orar, facultate, an, serie, grupa, semigrupa, singletimeevent, profesor, student, \
    customInclusion, notification, customExclusion

urlpatterns = [
    path('facultati/create', facultate.post, name='put_facultate'),
    path('facultati/get/<str:pk>', facultate.get, name='get_facultate'),
    path('facultati/get_all', facultate.gets, name='get_facultati'),
    path('facultati/delete/<str:pk>', facultate.delete, name='delete_facultate'),
    path('facultati/delete_all', facultate.deletes, name='delete_facultati'),

    path('ani/create', an.post, name='put_an'),
    path('ani/get/<str:pk>', an.get, name='get_an'),
    path('ani/get_all', an.gets, name='get_ani'),
    path('ani/get_from_facultate/<str:facultate>', an.get_from_facultate, name='get_ani_from_facultate'),
    path('ani/delete/<str:pk>', an.delete, name='delete_an'),
    path('ani/delete_all', an.deletes, name='delete_ani'),

    path('serii/create', serie.post, name='put_serie'),
    path('serii/get/<str:pk>', serie.get, name='get_serie'),
    path('serii/get_all', serie.gets, name='get_serii'),
    path('serii/get_from_an/<str:an>', serie.get_from_an, name='get_serii_from_an'),
    path('serii/delete/<str:pk>', serie.delete, name='delete_serie'),
    path('serii/delete_all', serie.deletes, name='delete_serii'),

    path('grupe/create', grupa.post, name='put_grupa'),
    path('grupe/get/<str:pk>', grupa.get, name='get_grupa'),
    path('grupe/get_all', grupa.gets, name='get_grupe'),
    path('grupe/get_from_serie/<str:serie>', grupa.get_from_serie, name='get_grupe_from_serie'),
    path('grupe/delete/<str:pk>', grupa.delete, name='delete_grupa'),
    path('grupe/delete_all', grupa.deletes, name='delete_grupe'),

    path('semigrupe/create', semigrupa.post, name='put_semigrupa'),
    path('semigrupe/get/<str:pk>', semigrupa.get, name='get_semigrupa'),
    path('semigrupe/get_all', semigrupa.gets, name='get_semigrupe'),
    path('semigrupe/get_from_grupa/<str:grupa>', semigrupa.get_from_grupa, name='get_semigrupe_from_grupa'),
    path('semigrupe/delete/<str:pk>', semigrupa.delete, name='delete_semigrupa'),
    path('semigrupe/delete_all', semigrupa.deletes, name='delete_semigrupe'),

    path('schedule/get_from_semigrupa/<str:id>', schedule.get_from_semigrupa, name='get_schedule_from_semigrupa'),

    path('student/register', student.register, name='register_student'),

    path('get_account_info', student.getAccountInfo, name='get_account_info'),
    path('schedule/get_personal', schedule.get_personal, name='get_my_own_schedule'),
    path('tema/get_personal', singletimeevent.get_teme, name='get_teme'),
    path('examen/get_personal', singletimeevent.get_examene, name='get_examene'),
    path('notification/get_personal', notification.get_notifications, name='get_schedule_notification'),
    path('schedule/include/create', customInclusion.post, name='create_custom_inc'),
    path('schedule/exclude/create', customExclusion.post, name='create_custom_exc'),
    path('schedule/exclude/get_personal', customExclusion.get, name='get_custom_exc'),
    path('schedule/include/get_personal', customExclusion.get, name='get_custom_inc'),
    path('schedule/include/delete/<str:pk>', customInclusion.delete, name='delete_custom_inc'),
    path('schedule/exclude/delete/<str:pk>', customExclusion.delete, name='delete_custom_exc'),

    path('profesor/register', profesor.register, name='register_profesor'),

    path('schedule/curs/create', schedule.add_curs, name='add_curs'),
    path('schedule/seminar/create', schedule.add_seminar, name='add_seminar'),
    path('schedule/laborator/create', schedule.add_laborator, name='add_laborator'),
    path('notification/create_course_notif', notification.create_notification_course, name='create_course_notif'),
    path('notification/create_seminar_notif', notification.create_notification_seminar, name='create_seminar_notif'),
    path('notification/create_lab_notif', notification.create_notification_lab, name='create_lab_notif'),
    path('tema/create', singletimeevent.post_tema, name='post_tema'),
    path('tema/delete/<str:pk>', singletimeevent.delete_tema, name='delete_tema'),
    path('examen/create', singletimeevent.post_examen, name='post_examen'),
    path('examen/delete/<str:pk>', singletimeevent.delete_examen, name='delete_examen'),

]
