from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="课程名称", blank=True,
                            null=True, default='Love English')
    scale = models.CharField(max_length=20, verbose_name="课程规模", blank=True,
                             null=True, default="5")
    age = models.CharField(max_length=20, verbose_name="年龄", blank=True,
                           null=True, default="5")
    evaluation = models.CharField(max_length=20, verbose_name="评分", blank=True,
                                  null=True, default="4")
    image = models.FileField(upload_to='blog/uploads/', verbose_name="课程图片")
    money = models.CharField(max_length=20, verbose_name="费用", blank=True,
                             null=True, default="4000")
    remain = models.CharField(max_length=10, verbose_name="剩余人数", blank=True,
                              null=True, default="2")
    teacher = models.CharField(max_length=255, verbose_name="课程教师", blank=True,
                               null=True, default='Love English')


class Teacher(models.Model):
    pass
