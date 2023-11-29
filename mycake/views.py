import json

from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests.auth import HTTPBasicAuth

#from mycake.credentials import LipanaMpesaPpassword, MpesaAccessToken,MpesaC2bCredential
from mycake.models import Customer,CakesAndEquipments

# Create your views here.
def register(request):
    if request.method =='POST':
        customer = Customer(firstName=request.POST['firstName'],lastName=request.POST['lastName'],
                       username=request.POST['userName'],password=request.POST['password'])
        customer.save()
        return redirect('login')
    else:
     return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    if request.method == 'POST':
        if Customer.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():

            customer = Customer.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request,'index.html', {'customer': customer})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def index(request):
    return render(request,'index.html')
def innerpage(request):
    return render(request,'innerpage.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def menu(request):
    return render(request,'menu.html')
def chefs(request):
    return render(request,'chefs.html')
def gallery(request):
    return render(request,'gallery.html')
def dropdown(request):
    return render(request,'dropdown.html')
def contact(request):
    return render(request,'contact.html')
def addproduct(request):
    if request.method == "POST":
        form = CakesAndEquipments(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addproduct')
    else:
        form = CakesAndEquipments()
        return render(request,'addproduct.html',{'form':form})
def show(request):
    cakesandequipments = CakesAndEquipments.objects.all()
    return render(request,'show.html',{'cakesandequipments':cakesandequipments})

def delete(request, id):
    products = CakesAndEquipments.objects.get(id=id)
    products.delete()
    return redirect('/show')
def edit(request,id):
    products = CakesAndEquipments.objects.get(id=id)
    return render(request,'edit.html',{'cakesandequipments': products})

def update(request,id):
    cakesandequipments = CakesAndEquipments.objects.get(id=id)
    form = CakesAndEquipments(request.POST,instance=cakesandequipments)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html',{'cakesandequipments':cakesandequipments})

def token(request):
    consumer_key = 'nUTOiX1tE1gvt7sP0dHvOTyHc3Fv79g1'
    consumer_secret = 'wPzOFI9opatpSBJU'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
    return render(request, 'pay.html')

#def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)
