from django.shortcuts import render
from django.http import HttpResponse
from .models import Information
# # Create your views here.
def blog(request):
    return HttpResponse ("This is my stady blog")

def get(request):
    infos=Information.objects.all()
    output=""
    for info in infos:
        output += f"id: {info.id} . name : {info.name}, roll : {info.roll}, age : {info.age}, dept : {info.dept} "
        
    return HttpResponse (output)

def info (request,dept):
    students=Information.objects.all()
    output=""
    if dept :   
        students=students.filter(dept="cst")  
    else:
        print("{student.dept} department student nopt found")
    for student in students:
          output += f"id : {student.id} , name : {student.name} , roll : {student.roll} , age : {student.dept}"
    return HttpResponse (output)

def list (request,age):
    students=Information.objects.all()
    output_list=[]
    if age :   
        students=students.filter(age__gt=21)  
    else:
        print("{student.dept} department student nopt found")
    for student in students:
        info_list=(
            f"ID : {student.id}\n"
            f"name : {student.name}\n"
            f"roll : {student.roll}\n"
            f"age : {student.age}\n"
            f"dept : {student.dept}"
        )
        output_list.append(info_list)
    output="\n".join(output_list)
    return HttpResponse (f"<pre>{output}</pre>")

def create(request):
    Information.objects.create(name="Rakib",roll=666123,age=23,dept="class and ciramix")
    return HttpResponse("data created successfully")
    
def read(request):
    output=""
    output=Information.objects.all().values('id','name','roll','age','dept')
    return HttpResponse (output)

# infos=Information.objects.all().values("id","name","roll","age","dept")
# print(infos)


def update(request,id):
    info=Information.objects.get(id=id)
    info.name="easin"
    info.roll=666214
    info.age=23
    info.dept="ET"
    info.save()
    return HttpResponse ("information update successfull")

def delete(request,id):
    info=Information.objects.get(id=id)
    info.delete()
    return HttpResponse (info)
    
    
def show(request):
    students=Information.objects.all()
    output=""
    for info in students:
        output += f"id : {info.id} \t name : {info.name} \t rolll : {info.roll} \t  age : {info.age} \t dept {info.dept} \n"
    return HttpResponse (f"<pre>{output}</pre>")