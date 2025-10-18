from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Student 
# Create your views here.
def student_list(request):
    info=Student.objects.all()
    if info :
        context={
            "data":info
        }
        return render (request,"student_list.html",context)
    else:
        return HttpResponse ("not availabl data from info")
    
    
def add_student(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        course=request.POST.get("course")
        
        print(name,age,course)
        
        data=Student(name=name,age=age,course=course)
        data.save()
        
        print("data create successfully")
        return redirect("student_list")                                                                                                     
                                                            
    return render(request,"student_form.html")
def update_student(request,id):
    info=Student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        course=request.POST.get("course")
        
        info.name=name
        info.age=age
        info.course=course
        info.save()
        return redirect ("student_list")
    
    context={
        "id":info.id,
        "name":info.name,
        "age":info.age,
        "course":info.course
    }
    return render (request,"student_update.html",context)

def delete_student(request,id):
    info=Student.objects.get(id=id)
    info.delete()    
    return redirect ("student_list")
