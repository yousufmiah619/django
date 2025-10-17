from django.urls import path
from .views import *

urlpatterns = [
    path("blog/",blog,name="blog"),
    path("get/",get,name="get"),
    path('info/<str:dept>',info,name="info"),
    path("list/<int:age>",list,name="list"),
    path("create/",create,name="create"),
    path("read/",read,name="read"),
    path("update/<int:id>",update,name="update"),
    path("delete/<int:id>",delete,name="delete"),
    path("show/",show,name="show"),
    path("page/",page,name="page"),
    path("view/<int:id>",get_data_by_id,name="get_data_by_id"),
    path("add-items/",add_items,name="add_items"),
    path("update-html/<int:id>/",update_html,name="update_page")
]
