from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode



# Create your models here.
class SignUp(models.Model):

    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp_add = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    timestamp_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.first_name)

#
# class UserNames(models.Model):
#     name = models.CharField(max_length=120, null=True, blank=True)
#
#     def __unicode__(self):
#         return smart_unicode(self.name)


# Create Login
class CreateLogin(models.Model):

    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=8, null=False, blank=False)

    def __unicode__(self):
        return smart_unicode(self.first_name)

