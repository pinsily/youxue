from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from . import models


# Create your views here.

def index(request):
    courses = models.Course.objects.all()

    data = {
        'courses': courses,
        'page': 'index',
    }

    return render(request, 'dutch/index.html', data)


def detail(request):
    return render(request, 'dutch/detail.html')


def search(request):
    return render(request, 'dutch/index.html')


class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'dutch/detail.html'
    context_object_name = 'course'

    # 接受来自 url 中的参数
    pk_url_kwarg = 'course_id'

    # 从数据库中获取相应ID文章、
    def get_object(self, queryset=None):
        obj = super(CourseDetailView, self).get_object()

        obj.class_target = obj.class_target.split("\r\n")
        # print(obj.class_target)

        return obj

    # 为模板添加分类和标签上下文变量
    def get_context_data(self, **kwargs):
        kwargs["page"] = "detail"
        return super(CourseDetailView, self).get_context_data(**kwargs)


@csrf_exempt
def startclass(request):
    if request.is_ajax():
        user_name = request.POST.get('idname', False)
        user_phone = request.POST.get('userphone', False)
        user_qq = request.POST.get('userqq', False)
        user_wechat = request.POST.get('userwechat', False)
        class_id = request.POST.get('id', False)

        class_name = request.POST.get('class_name', False)
        class_address = request.POST.get('class_address', False)
        class_time = request.POST.get('class_time', False)
        class_people = request.POST.get('class_people', False)
        class_age = request.POST.get('class_age', False)
        teacher_gender = request.POST.get('teacher_gender', False)
        teacher_name = request.POST.get('teacher_name', False)

        ret_data = {'ret_code': '200', 'ret_message': '发起成功, 稍后请等待客服联系'}

        course = models.Course()

        course.name = class_name
        course.address = class_address
        course.scale = class_people
        course.remain = class_people
        course.age = class_age
        course.teacher_name = teacher_name
        course.class_time_all = class_time

        course.save()

        models.ClassUser.objects.create(name=user_name,
                                        telphone=user_phone, qq=user_qq,
                                        wechat=user_wechat, course=course,
                                        sponsor="1")
        return JsonResponse(ret_data)

    return render(request, 'dutch/startClass.html', {"page": "start"})


@csrf_exempt
def join_class(request):
    try:
        if request.is_ajax():
            username = request.POST.get('idname', False)
            userphone = request.POST.get('userphone', False)
            userqq = request.POST.get('userqq', False)
            userwechat = request.POST.get('userwechat', False)
            class_id = request.POST.get('id', False)

            ret_data = {'ret_code': '200', 'ret_message': '加入成功, 稍后请等待客服联系'}

            # 存储拼班人员信息
            course = models.Course.objects.get(id=class_id)

            if int(course.remain) == 0:
                ret_data["ret_code"] = "300"
                ret_data["ret_message"] = "报班人数已满，抱歉!"
                return JsonResponse(ret_data)

            models.ClassUser.objects.create(name=username,
                                            telphone=userphone, qq=userqq,
                                            wechat=userwechat, course=course,
                                            sponsor="0")

            return JsonResponse(ret_data)
    except:
        ret_data = {'ret_code': '300', 'ret_message': "加入失败!"}
        return JsonResponse(ret_data)


def userpage(request):
    return render(request, 'dutch/userpage.html', {"page": "user"})


# 课程列表
def dutch(request):
    dutchs = models.Dutch.objects.all()
    kwargs = {
        'page': "dutch",
        'dutchs': dutchs
    }
    return render(request, 'dutch/dutch.html', kwargs)


def teacher(request):
    teachers = models.Teacher.objects.all()
    kwargs = {
        'page': 'teacher',
        'teachers': teachers
    }
    return render(request, 'dutch/teachers.html', kwargs)