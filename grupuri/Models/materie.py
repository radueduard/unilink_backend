import uuid

from django.db import models

from .grupa import Grupa
from .profesor import Profesor
from .semigrupa import Semigrupa
from .serie import Serie


class Materie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nume = models.CharField(max_length=50, default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Materia " + self.nume.__str__()


class Curs(Materie):
    profesor = models.ForeignKey(Profesor, related_name="cursuri", on_delete=models.SET_NULL, default=0, null=True)
    serie = models.ForeignKey(Serie, related_name="cursuri", on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "Cursul " + self.nume.__str__() + " de la " + self.serie.__str__() + ' ' + self.id.__str__()


class Seminar(Materie):
    seminarist = models.ForeignKey(Profesor, related_name="seminare", on_delete=models.SET_NULL, default=0, null=True)
    grupa = models.ForeignKey(Grupa, related_name="seminare", on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "Seminarul " + self.nume.__str__() + " de la " + self.grupa.__str__()


class Laborator(Materie):
    asistent = models.ForeignKey(Profesor, related_name="laboratoare", on_delete=models.SET_NULL, default=0, null=True)
    semigrupa = models.ForeignKey(Semigrupa, related_name="laboratoare", on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "Laboratorul " + self.nume.__str__() + " de la " + self.semigrupa.__str__()
