from django.db import models

from School.models import Standard, Subject
from members.models import Student, Teacher


class Assignment(models.Model):
    asign_topic = models.CharField(max_length=2000)
    asign_date = models.DateField()
    asign_class = models.ForeignKey(Standard)
    asign_teacher = models.ForeignKey(Teacher)
    asign_subject = models.ForeignKey(Subject)


class AssignmentStatus(models.Model):
    given_assignment = models.ForeignKey(Assignment)
    student = models.OneToOneField(Student)
    student_completion_status = models.BooleanField(default=False)
    parent_verify_status = models.BooleanField(default=False)
    teachers_remark = models.CharField(max_length=20)
    parent_remark = models.CharField(max_length=20)


class Attendance(models.Model):
    attendent = models.ForeignKey(Student)
    atdnc_presence = models.BooleanField(default=False)
