from django.db import models

# Create your models here.
from django.urls import reverse


class Course(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now=True)
    teacher_name = models.CharField(max_length=255, verbose_name="教师名称", blank=True,
                                    null=True)
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
    teacher = models.ForeignKey('Teacher', verbose_name="课程教师", on_delete=models.DO_NOTHING, null=True)
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


class ClassUser(models.Model):
    name = models.CharField(max_length=255, verbose_name="家长姓名")
    telphone = models.CharField(max_length=11, verbose_name="电话")
    qq = models.CharField(max_length=30, verbose_name="QQ")
    wechat = models.CharField(max_length=20, verbose_name="wechat")
    sponsor = models.CharField(max_length=1, verbose_name="是否为发起人")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Classuser"


class DutchClass(models.Model):
    name = models.CharField(max_length=255, verbose_name="课程分类名称")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dutchclass"
        ordering = ["name"]


class Dutch(models.Model):
    name = models.CharField(max_length=255, verbose_name="课程名称")
    detail = models.TextField(verbose_name="课程简介", help_text="取前50字")
    detail_url = models.URLField(verbose_name="推文链接", help_text="跳转到推文链接")
    image = models.FileField(null=True, blank=True, upload_to='dutch/', default="dutch/default.png", help_text="图片")
    dutch_class = models.ForeignKey(DutchClass, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dutch"
        ordering = ["name"]
