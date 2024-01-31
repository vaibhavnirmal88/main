from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import Receipt
from Receipt.models import Receipts


def preceipt(request,id):
    receiptdata=Receipts.objects.get(receipt_number=id)
    data={'receiptdata':receiptdata}
    return render(request,"receipt.html",data)

def receipt_form(request):
    fn=Receipt()
    data={'form':fn}
    return render(request,"receipt_form.html",data)

def receipt(request):
    if request.method=="POST":
        name=request.POST.get('name')
        date=request.POST.get('date')
        email=request.POST.get('email')
        mobile_number=request.POST.get('mobile_number')
        amount=request.POST.get('amount')
        month=int(date[5:7])
        year=int(date[0:4])
        if month > 6:
            years= f"{year}-{year+1}"  
        else :
            years= f"{year-1}-{year}"

    data={
        'name':name,
        'date':date,
        'email':email,
        'mobile_number':mobile_number,
        'years':years,
        'amount':amount
    }
    en=Receipts(Name=name,date=date,email=email,mobile_number=mobile_number,amount=amount,years=years)
    en.save()
    return render(request,"receipt.html",data)