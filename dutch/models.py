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
    people_num = models.CharField(max_length=10, verbose_name="人数", default="2")
    class_target = models.TextField(verbose_name="课程目标")
    class_period = models.CharField(max_length=255, verbose_name="课程周期", default='一周两节课，一期两个月')
    class_time_all = models.CharField(max_length=255, verbose_name="课程时间", default='周六下午 15:00-16:30')
    class_time_one = models.CharField(max_length=255, verbose_name="单节课程时间", default='45', help_text="分钟")

    image = models.FileField(null=True, blank=True, upload_to='course/', default="course/default.png")

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
    experience = models.CharField(max_length=4, verbose_name="工作经验", help_text="年", blank=True, null=True)
    come_from = models.CharField(max_length=10, verbose_name="国家", blank=True, null=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间')

    image = models.FileField(null=True, blank=True, upload_to='teacher/', default="teacher/default.jpg")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teeacher"
