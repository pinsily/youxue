from . import models
import xadmin


# 自定义右侧菜单栏
class GlobalSetting(object):
    site_title = "行橙拼班"
    site_footer = '行橙拼班'


xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)


class CourseAdmin(object):
    pass


class TeacherAdmin(object):
    pass


class ClassUserAdmin(object):
    pass


class DutchAdmin(object):
    pass


class DutchClassAdmin(object):
    pass


xadmin.site.register(models.Course, CourseAdmin)
xadmin.site.register(models.Teacher, TeacherAdmin)
xadmin.site.register(models.ClassUser, ClassUserAdmin)
xadmin.site.register(models.DutchClass, DutchClassAdmin)
xadmin.site.register(models.Dutch, DutchAdmin)
