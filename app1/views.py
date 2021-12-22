from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.db.models import Q

def index(request):
    a=Product.objects.all()
    s=request.GET.get('search')

    if s:
        q=Product.objects.filter(Q(name__icontains=s) | Q(des__icontains=s))
        if not q:
            return HttpResponse("<h1>Not Item Available.....</h1>")
    else:
        q=Product.objects.all()
    return render(request,'test.html',{'abc':a,'pro':q})

    # try:
    #     q = request.GET.get('search')
    # except:
    #     q = None
    # if q:
    #     pro= Product.objects.filter(Q(name__icontains=q) | Q(price__icontains=q) | Q(des__icontains=q))
    # else:
    #     data={}
    # return render(request, 'test.html',{'abc':a,'pro':pro})
# Create your views here.
