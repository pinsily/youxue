from django.db import models


# Create your models here.
from django.urls import reverse


class Course(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    created_time = models.DateTimeField(verbose_name=u'创建时间')
    name = models.CharField(max_length=255, verbose_name="课程名称", blank=True,
                            null=True, default='Love English')
    scale = models.CharField(max_length=20, verbose_name="课程规模", blank=True,
                             null=True, default="5")
    age = models.CharField(max_length=20, verbose_name="年龄", blank=True,
                           null=True, default="5")
    evaluation = models.CharField(max_length=20, verbose_name="评分", blank=True,
                                  null=True, default="4")
    lesson_money = models.CharField(max_length=20, verbose_name="单节课程费用", blank=True,
                                    null=True, default="258")
    money = models.CharField(max_length=20, verbose_name="费用", blank=True,
                             null=True, default="4000")
    remain = models.CharField(max_length=10, verbose_name="剩余人数", blank=True,
                              null=True, default="2")
    teacher = models.ForeignKey('Teacher', verbose_name="课程教师", on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255, verbose_name="地址")
    people_num = models.CharField(max_length=10, verbose_name="剩余人数", default="2")
    class_target = models.TextField(verbose_name="课程目标")
    class_period = models.CharField(max_length=255, verbose_name="课程周期", default='一周两节课，一期两个月')
    class_time = models.CharField(max_length=255, verbose_name="课程周期", default='周六下午 15:00-16:30')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        db_table = "course"

    def get_absolute_url(self):
        return reverse('dutch:detail', args=[str(self.id)])


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name="教师名称")
    introduce = models.TextField(verbose_name="教师简介")
    created_time = models.DateTimeField(verbose_name=u'创建时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teeacher"
