from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __unicode__(self):
        return u'%s of %s' (self.name, self.state)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, related_name='students')

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
