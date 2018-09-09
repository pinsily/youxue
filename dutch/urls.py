from django.urls import path

from dutch import views

app_name = 'dutch'

urlpatterns = [

    path('', views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("search/", views.search, name="search"),

]
