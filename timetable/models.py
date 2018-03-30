from django.db import models

from School.models import Standard, Subject
from members.models import Teacher


class Schedule(models.Model):
    standard = models.ForeignKey(Standard)
    day = models.CharField(max_length=30)
    time = models.TimeField()
    sub = models.ForeignKey(Subject)
    sub_teacher = models.ForeignKey(Teacher)
