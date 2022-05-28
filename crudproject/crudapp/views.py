from django.shortcuts import render,redirect
from .models import Detail
from .forms import detailsform
# Create your views here.
def home(request):
    return render(request,'index.html')
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        user=Detail.objects.create(name=name,age=age,address=address)
        user.save()
        print("user created")
        return redirect('/')   
def read(request):
    detail=Detail.objects.all()
    return render(request,'read.html',{'detail':detail})   


def edit(request,id):
    
    object=Detail.objects.get(id=id)
    return render(request,'update.html',{'object':object})
    
def update(request,id):
    object=Detail.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=Detail.objects.all()
        return redirect('read')
def delete(request,pk):   
        Detail.objects.filter(id=pk).delete()
        return redirect('read')