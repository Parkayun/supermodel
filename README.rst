supermodel
==========


Remote ORM. (currently, it's for Django)


Installing
~~~~~~~~~~

This is under development, You should install via Github.

.. sourcecode:: bash

   ~ $ pip install git+https://github.com/Parkayun/supermodel.git


Quick start
~~~~~~~~~~~

client

.. sourcecode:: python

   from django.db import models
   
   from supermodel import RemoteModel

  
   class Books(RemoteModel):
   
       __host__ = 'http://host'

       name = models.CharField(max_length=10)
       created_at = models.DateTimeField(auto_now_add=True)

server

.. sourcecode:: python

   '''Wait for it'''

