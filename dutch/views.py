from django.shortcuts import render
from django.views.generic import DetailView

from . import models


# Create your views here.

def index(request):
    courses = models.Course.objects.all()

    data = {
        'courses': courses,
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
        print(obj.class_target)

        return obj

    # 为模板添加分类和标签上下文变量
    def get_context_data(self, **kwargs):
        return super(CourseDetailView, self).get_context_data(**kwargs)


def startclass(request):
    return render(request, 'dutch/startClass.html')
