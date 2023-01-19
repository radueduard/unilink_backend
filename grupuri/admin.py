from django.contrib import admin

from .Models.customSchedule import CustomExclusion, CustomInclusion
from .Models.facultate import Facultate
from .Models.an import An
from .Models.materie import Curs, Seminar, Laborator
from .Models.notification import NotificationSchedule, NotificationLab, NotificationSeminar, NotificationCourse
from .Models.profesor import Profesor
from .Models.sala import Sala
from .Models.schedule import Schedule, ScheduleC, ScheduleS, ScheduleL
from .Models.serie import Serie
from .Models.grupa import Grupa
from .Models.semigrupa import Semigrupa
from .Models.student import Student
from .Models.singletimeevent import Tema, Examen


# Register your models here.

admin.site.register(Facultate)
admin.site.register(An)
admin.site.register(Serie)
admin.site.register(Grupa)
admin.site.register(Semigrupa)

admin.site.register(Curs)
admin.site.register(Seminar)
admin.site.register(Laborator)

admin.site.register(Profesor)
admin.site.register(Student)

admin.site.register(Sala)

admin.site.register(Schedule)
admin.site.register(ScheduleC)
admin.site.register(ScheduleS)
admin.site.register(ScheduleL)

admin.site.register(CustomExclusion)
admin.site.register(CustomInclusion)

admin.site.register(Tema)
admin.site.register(Examen)

admin.site.register(NotificationCourse)
admin.site.register(NotificationSeminar)
admin.site.register(NotificationLab)
