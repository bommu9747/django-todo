from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def todos(request):
    data=Task.objects.all()
    print(data)
    return render(request,'index.html',{'data':data})
def add(request):
    if request.method =='POST':
        name = request.POST['task']
        priority=request.POST['Priority']
        date =request.POST['date']
        task2=Task(name=name,priority=priority,date=date)
        task2.save()
        data=Task.objects.all()
        return render(request,'index.html',{'data':data})
    return render(request,'index.html')


def delete(request,dele):
    add=Task.objects.get(id=dele)
    add.delete()
    return redirect('todo')

def edit(request,ed):
    data=Task.objects.get(id=ed)
    return render(request,'edit.html',{'data':data})
def formupdate(request,con):
    if request.method=='POST':
        ADD=Task.objects.get(id=con)
        ADD.name=request.POST['task']
        ADD.date=request.POST['date']
        ADD.priority=request.POST['Priority']
        ADD.save()
    return redirect('todo')
    
    

    
