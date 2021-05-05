from django.shortcuts import render, HttpResponse, redirect
from sohal.models import Task
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request,user)
            return redirect('sohal')
        else:
            messages.info(request,'User name or password is incorrect')
            
    context={}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
      form = UserCreationForm()
      context = {'form':form}
      return render(request,'register.html',context)

@login_required(login_url='login')
def sohal(request):
    context = {'success': False}
    if request.method == "POST":
        #handle the form
        collectionDt = request.POST['collectionDt']
        DispatchDt = request.POST['DispatchDt']
        ShipNo = request.POST['ShipNo']
        SDMNo = request.POST['SDMNo']
        ModelNo = request.POST['ModelNo']
        ChassisNo = request.POST['ChassisNo']
        From = request.POST['From']
        To = request.POST['To']
        DealerName = request.POST['DealerName']
        DelDate = request.POST['DelDate']
        Status = request.POST['Status']
        Drivername = request.POST['Drivername']
        contact = request.POST['contact']
        Distance = request.POST['Distance']
        Average = request.POST['Average']
        HSDpump = request.POST['HSDpump']
        CashOnHand = request.POST['CashOnHand']
        DeiselDRate = request.POST['DeiselDRate']
        TotalDeisel = request.POST['TotalDeisel']
        DriverPayment = request.POST['DriverPayment']
        Tax = request.POST['Tax']
        OtherExpenses = request.POST['OtherExpenses']
        TotalBillAmnt = request.POST['TotalBillAmnt']
        Taxableamnt = request.POST['Taxableamnt']
        Igst = request.POST['Igst']
        TotalBillingAmount = request.POST['TotalBillingAmount']
        Poddt = request.POST['Poddt']
        BillNo = request.POST['BillNo']
        BillDt = request.POST['BillDt']
        
        ins = Task(taskcollectionDt = collectionDt,
        taskDispatchDt = DispatchDt,
        taskShipNo = ShipNo,
        taskSDMNo = SDMNo,
        taskModelNo = ModelNo,
        taskChassisNo = ChassisNo,
        taskFrom = From,
        taskTo = To,
        taskDealerName = DealerName,
        taskDelDate = DelDate,
        taskStatus = Status,
        taskDrivername = Drivername,
        taskcontact = contact,
        taskDistance = Distance,
        taskAverage = Average,
        taskHSDpump = HSDpump,
        taskCashOnHand = CashOnHand,
        taskDeiselDRate = DeiselDRate,
        taskTotalDeisel = TotalDeisel,
        taskDriverPayment = DriverPayment,
        taskTax = Tax,
        taskOtherExpenses = OtherExpenses,
        taskTotalBillAmnt = TotalBillAmnt,
        taskTaxableamnt = Taxableamnt,
        taskIgst = Igst,
        taskTotalBillingAmount = TotalBillingAmount,
        taskPoddt = Poddt,
        taskBillNo = BillNo,
        taskBillDt =  BillDt)
        ins.save()
        context = {'success': True}


    return render(request,'mainPage.html', context)
@login_required(login_url='login')
def Data(request):
    allData = Task.objects.all()
    context = {'tasks':allData}
    return render(request,'Data.html',context)

@login_required(login_url='login')
def update(request,pk):
    update = Task.objects.get(id=pk)
    form = Taskform(instance=update)
    if request.method == 'POST':
       form = Taskform(request.POST,instance=update)
       if form.is_valid():
           form.save()
           return redirect('/') 
    context = {'forms': form} 
    return render(request,'update.html',context)
@login_required(login_url='login')
def deleteData(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/') 
    return render(request,'delete.html',context)



