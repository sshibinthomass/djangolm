from django.shortcuts import render
from leaverequest.models import leaveDetails
# Create your views here.
def leaverequest(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        regno=request.POST['regno']
        dept=request.POST['dept']
        year=request.POST['year']
        reason=request.POST['reason']
        startDate=request.POST['startDate']
        endDate=request.POST['endDate']
        writ=leaveDetails(name=name,phone=phone,email=email,regno=regno,dept=dept,year=year,reason=reason,startDate=startDate,endDate=endDate)
        writ.save()
    return render(request,'leaverequest.html')