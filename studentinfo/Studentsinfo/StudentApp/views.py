from django.shortcuts import render , HttpResponse ,redirect
from .models import studinfo
# Create your views here.
def index(req):
    #This Code is for creating records
    if req.method =="POST":
        print(req.method)
        name = req.POST.get('sname',False)
        mail = req.POST.get('mail',False)
        phone = req.POST.get('phone',False)
        address= req.POST.get('address',False)
        data = studinfo(sname=name,mail=mail,address=address,phone=phone)
        
        data.save()
        return redirect('index')
    
    #for retriving Data on index Page
    d = studinfo.objects.all()
    context = {"d":d}
    return render(req,'index.html',context)
#updating records
def updateStudent(req,id):
    d = studinfo.objects.get(id=id)
    if req.method =="POST":
        print(req.method)
        name = req.POST.get('sname',False)
        mail = req.POST.get('mail',False)
        phone = req.POST.get('phone',False)
        address= req.POST.get('address',False)
        d = studinfo(id = id,sname=name,mail=mail,address=address,phone=phone)

        d.save()
        return redirect("index")

#deleting Records
def deleteStudent(req,id):
    d = studinfo(id=id)
    d.delete()
    return redirect("index")

# delete All students 
def deleteAllstudents(req):
    d = studinfo.objects.all()
    d.delete()
    return redirect("index")