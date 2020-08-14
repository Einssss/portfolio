from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.allblogs, name="AllBlogs"),
    path('<int:blog_id>/',views.detail, name='detail')
]