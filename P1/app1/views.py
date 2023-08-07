from django.shortcuts import render
from .models import details

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        age = request.POST.get('age',0)

        obj = details()
        obj.name = name
        obj.age = age
        obj.save()
        return render(request,'index.html',{'name':name,'age':age})
    return render(request,'index.html')