import uuid
from enum import Enum
from django.db import models

from account.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Tip(Enum):
    ERR = 0
    PROFESOR = 1 << 0
    ASISTENT = 1 << 1
    SEMINARIST = 1 << 2


class Profesor(Account):
    def __str__(self):
        return self.username


@receiver(post_save, sender=Profesor)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)