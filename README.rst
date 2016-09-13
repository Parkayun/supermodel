supermodel
==========


Remote ORM. (currently, it's for Django)


Installing
~~~~~~~~~~

This is under development, You should install via Github.

.. sourcecode:: bash

   ~ $ pip install git+https://github.com/Flative/supermodel.git


Quick start
~~~~~~~~~~~

server

.. sourcecode:: python
    from django.db import models


    class Books(models.Model):

        name = models.CharField(max_length=10)

.. sourcecode:: python

   from supermodel.views import MODELS, api

   from common.models import Books


   MODELS.update({'Books': Books})

   end_point_view = api

.. sourcecode:: sh

    $ python manage.py makemigration
    $ python manage.py migrate
    $ python manage.py shell
    >>> from common.models import Books
    >>> Books.objects.create(name='test')

client

.. sourcecode:: python

   from django.db import models

   from supermodel import RemoteModel

  
   class Books(RemoteModel):
   
       __host__ = 'http://host/end_point_url'

       name = models.CharField(max_length=10)

.. sourcecode:: python

    from common.models import Books
    print(Books.objects.all())
    [<Books: Books object>] # Tada


Insert `supermodel` into `INSTALLED_APPS` on `settings.py` (server and client projects).

