from django.db import models
from django.db.models.manager import Manager


class RemoteManager(Manager):

    def all(self):
        pass

    def filter(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass


class RemoteModel(models.Model):

    objects = RemoteManager()

    class Meta:
        abstract = True

