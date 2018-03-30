from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.functions import datetime

from School.models import Subject, Standard


class Teacher(models.Model):
    tr_name = models.OneToOneField(User)
    tr_subjects = models.ManyToManyField(Subject)


class Student(models.Model):
    stdnt_name = models.OneToOneField(User)
    stdnt_class = models.OneToOneField(Standard, blank=True, null=True)
    stdnt_roll_no = models.IntegerField()
    stdnt_gender = models.CharField(max_length=6)
    stdnt_birthday = models.DateTimeField()
    stdnt_mobile_no = models.IntegerField()

    @property
    def age(self):
        return (datetime.datetime.now() - self.stdnt_birthday).days // 365


class Parent(Student):
    parent_name = models.OneToOneField(User, blank=True, null=True)
