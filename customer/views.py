from email import message
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from customer.forms import CustomerForm
from customer.models import CustomerModel
from django.contrib.auth.decorators import login_required


# def customer(request):
#     data = CustomerModel.objects.all()
#     form = CustomerForm()
#     if request.method == "POST":
#         customer = CustomerForm(request.POST)
#         if customer.is_valid():
#             customer.save()
#             return redirect('/')
#         else:
#             messages.info("Something Wrong")
#     context = {'data':data, 'form':form}
#     return render(request, "home.html", context)
@login_required(login_url='/accounts/')
def customer(request):
    form_customer = CustomerModel.objects.all()
    return render(request, 'customer.html', {'data':form_customer})

@login_required(login_url='/accounts/')
def create_customer(request):
    form_customer = CustomerForm()
    if request.method == 'POST':
        customer = CustomerForm(request.POST)
        if customer.is_valid():
            customer.save()
            return redirect('/')
        else:
            return HttpResponse("SomethingWrong")  
    else:
        return render(request, 'add_custumer.html', {'form':form_customer})

@login_required(login_url='/accounts/')
def detail_customer(req, id):
    detail_customer = CustomerModel.objects.get(id=id)
    data = CustomerForm(detail_customer, many=False)
    data1 = data.data    
    return render(req, 'customer_detail.html', {
        'data': data1,
    })

@login_required(login_url='/accounts/')
def delete_customer(req, id):
    CustomerModel.objects.get(id=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/')
    
@login_required(login_url='/accounts/')
def update_customer(req, id):
    if req.POST:
        data = CustomerModel.objects.filter(pk=id).update(
            name=req.POST['name'], 
            phone=req.POST['phone'], 
            address=req.POST['address'], 
            date=req.POST['date'])
        return redirect('/customer/')

    data = CustomerModel.objects.filter(pk=id).first()    
    return render(req, 'customer_update.html', {
        'data': data,
    })