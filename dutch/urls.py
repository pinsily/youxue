from django.urls import path, re_path

from dutch import views

app_name = 'dutch'

urlpatterns = [

    path('', views.index, name="index"),
    re_path(r'^article/(?P<course_id>\d+)$',
            views.CourseDetailView.as_view(), name='detail'),
    path('joinclass/', views.join_class, name='joinclass'),
    # path("detail/", views.detail, name="detail"),
    path("search/", views.search, name="search"),
    path("startclass/", views.startclass, name="startclass"),
    path("userpage/", views.userpage, name="userpage")

]
