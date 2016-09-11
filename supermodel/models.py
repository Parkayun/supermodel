import requests

from django.db import models
from django.db.models.manager import Manager


class RemoteManager(Manager):

    def __make_object(self, fields):
        obj = self.model()
        for key, value in fields.items():
            setattr(obj, key, value)
        return obj

    def __request(self, parameters):
        url = self.model.host
        return requests.post(url, data=parameters).json()

    def _get_data(self, parameters=None):
        parameters = parameters if isinstance(parameters, dict) else {}
        data = self.__request(parameters)
        results = None

        if isinstance(data, list):
            results = []
            for fields in data:
                results.append(self.__make_object(fields))

        elif isinstance(data, dict):
            results = self.__make_object(data)

        return results

    def all(self):
        return self._get_data()

    def filter(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass


class RemoteModel(models.Model):

    objects = RemoteManager()

    class Meta:
        abstract = True

