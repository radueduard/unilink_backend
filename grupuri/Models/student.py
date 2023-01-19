from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .semigrupa import Semigrupa
from account.models import Account


class Student(Account):
    semigrupa = models.ForeignKey(Semigrupa, related_name="studenti", default='', on_delete=models.SET_DEFAULT)


@receiver(post_save, sender=Student)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
