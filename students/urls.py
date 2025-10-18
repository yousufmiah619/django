from django.urls import path
from .views import *

urlpatterns = [
    path("student-list/",student_list,name="student_list"),
    path("add-student/",add_student,name="add_student"),
    path("update-student/<int:id>/",update_student,name="update_student"),
    path("delete-student/<int:id>",delete_student,name="delete_student")
]
