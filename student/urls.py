from django.urls import path
from . import views

urlpatterns = [
    path("blog/",views.blog,name="student.blog"),
    path("get/",views.get,name="student.get"),
    path('info/<str:dept>',views.info,name="student.info"),
    path("list/<int:age>",views.list,name="student.list"),
    path("create/",views.create,name="student.create"),
    path("read/",views.read,name="student.read"),
    path("update/<int:id>",views.update,name="student.update"),
    path("delete/<int:id>",views.delete,name="student.delete"),
    path("show/",views.show,name="student.show")
]
