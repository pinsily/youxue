from . import models
import xadmin


class CourseAdmin(object):
    pass


class TeacherAdmin(object):
    pass


xadmin.site.register(models.Course, CourseAdmin)
xadmin.site.register(models.Teacher, TeacherAdmin)
