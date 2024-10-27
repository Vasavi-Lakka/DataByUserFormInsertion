from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

'''
def insertTopic(request):
    
    if request.method=='POST':
        #return HttpResponse(request.POST['tn'])
    
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn} is created')
    

    return render(request, 'insertTopic.html')



def insertWebpage(request):
    
    if request.method=='POST':
        #return HttpResponse(request.POST['tn'])
    
        tn=request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        n=request.POST['n']
        u=request.POST['u']
        WO=webpage.objects.get_or_create(topic_name=TO,name=n, url=u)
       


        return HttpResponse(f'{tn} is created')
    

    return render(request, 'insertWebpage.html')


def insertAccess(request):
    
    if request.method=='POST':
        #return HttpResponse(request.POST['tn'])
    
        n=request.POST['n']
        WO=webpage.objects.get(name=n)
        a=request.POST['a']
        d=request.POST['d']
        e=request.POST['e']
        AO=AccessRecord.objects.get_or_create(name=WO, author=a, date=d,email=e)
       


        return HttpResponse(f'{n}, {a}, {d}, {e} is created')
    

    return render(request, 'insertAccess.html')'''


def insertTopic(request):
    
    if request.method=='POST':
        #return HttpResponse(request.POST['tn'])
    
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn} is created')
    

    return render(request, 'insertTopic.html')


def insertWebpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    
    if request.method=='POST':
        #return HttpResponse(request.POST['tn'])
    
        tn=request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        n=request.POST['n']
        u=request.POST['u']
        WO=webpage.objects.get_or_create(topic_name=TO,name=n, url=u)
        return HttpResponse(f'{tn} is created')
    

    return render(request, 'insertWebpage.html', d)


def insertAccess(request):
    LWO=webpage.objects.all()
    d={'LWO':LWO}
    
    if request.method=='POST':
        #return HttpResponse(request.POST['tn'])
    
        n=request.POST['n']
        WO=webpage.objects.get(id=n)
        a=request.POST['a']
        d=request.POST['d']
        e=request.POST['e']
        AO=AccessRecord.objects.get_or_create(name=WO, author=a, date=d,email=e)
       


        return HttpResponse(f'{n}, {a}, {d}, {e} is created')
    

    return render(request, 'insertAccess.html', d)


def selectMultiple(request):
    LTO=Topic.objects.all()
    d={'LTO': LTO}

    if request.method=="POST":
        MTN=request.POST.getlist('tn')#multipleTopicName
        EQST=webpage.objects.none()#emptyQueryList
        for topic in MTN:
            EQST=EQST|webpage.objects.filter(topic_name=topic)
        d1={'EQST':EQST}
        return render(request, 'displayWebpage.html', d1)
    return render(request, 'selectMultiple.html', d)


def selectMultipleAccess(request):
    LWO=webpage.objects.all()
    d={'LWO':LWO}

    if request.method=="POST":
        MN=request.POST.getlist('n')#mutipleNames
        EQSN=AccessRecord.objects.none()#EmptyquerySETNames
        for name in MN:
            EQSN=EQSN|AccessRecord.objects.filter(name=name)
        d1={'EQSN':EQSN}
        return render(request, 'displayAccess.html', d1)
    return render(request, 'selectMultipleAccess.html', d)



def checkBox(request):
    LTO=Topic.objects.all()
    d={'LTO': LTO}
 
 
    return render(request, 'checkBox.html', d)

