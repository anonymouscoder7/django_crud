from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from myapp.models import Customers

def index_view(request):

    return render(request, 'index.html')

def about_view(request):
    cus =  Customers.objects.all()
    context = {
        'customer':cus,
    }
    return render(request, 'about.html',context)


def add_view(request):
    if request.method == "POST":
        name=request.POST['name']
        desc=request.POST['desc']

        cus = Customers(
            name = name,
            desc =desc,
        )
        cus.save()
        return redirect('about')
    
def edit_view(request,id):
    # idd = int(request.GET["id"])
    customer =Customers.objects.get(id=id)
    print("edit",customer.__dict__)
    #if form is submitted then update the data in database and go to home page
    if request.method=="POST" :
        new_name=request.POST['name']
        new_desc=request.POST['desc']
        customers = Customers.objects.filter(id=id).update(
            name=new_name , desc=new_desc,)
        return redirect('/about')
    else:
        context={
            'customers'   :    customer
            }
        return render (request,'edit.html',context)

def delete_view(request,id):
    customer =Customers.objects.get(id=id)
    customer.delete()
    return redirect ('about')
