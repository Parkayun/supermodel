import json

import requests

from django.db import models
from django.db.models.manager import Manager


class RemoteManager(Manager):

    def __make_object(self, fields):
        obj = self.model()
        for key, value in fields.items():
            setattr(obj, key, value)
        return obj

    def __request(self, parameters, method):
        url = self.model.__host__
        headers = {
            'X-MODEL': self.model._meta.object_name,
            'X-METHOD': method
        }
        return json.loads(requests.post(url, headers=headers, data=parameters).content.decode('utf-8'))

    def _get_data(self, parameters=None, method=None):
        parameters = parameters if isinstance(parameters, dict) else {}
        method = method if isinstance(method, str) and method in ('all', 'filter', 'get') else 'all'
        data = self.__request(parameters, method)
        results = None

        if isinstance(data, list):
            results = []
            for fields in data:
                results.append(self.__make_object(fields))

        elif isinstance(data, dict):
            results = self.__make_object(data)

        return results

    def all(self):
        return self._get_data(method="all")

    def filter(self, *args, **kwargs):
        return self._get_data(kwargs, method="filter")

    def get(self, *args, **kwargs):
        return self._get_data(kwargs, method="get")


class RemoteModel(models.Model):

    objects = RemoteManager()

    class Meta:
        abstract = True

