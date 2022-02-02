from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Signup,Category,Mycart,Product,Table,bookingdate
from django.db.models import Q
from .forms import editform
from .forms import signupforms
import smtplib, ssl
from django.contrib import messages
import random

def register(request):
    if request.method=="POST":
        obj=Signup()
        obj.username=request.POST['username']
        obj.email=request.POST['email']
        obj.phone=request.POST['phone']
        obj.password=request.POST['password']
        print(obj.password)
        obj.confirmpassword=request.POST['confirm-password']

        if obj.confirmpassword==obj.password:
            obj.save()
            return redirect('login')
        else:
            return HttpResponse('wrong password')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        try:
            e=request.POST['email']
            request.session['email']=e
            print(e)
            p=request.POST['password']
            print(e,p)
            x=Signup.objects.get(email=e)
            if x.password==p:
                messages.success(request, f'you are now logged')
                print(e)
                return redirect('index')
            else:
                messages.warning(request, 'Please input correct password')
        except:
            messages.warning(request,'Email wrong')
    return render(request,'login.html')

def forgot_pass(request):
    email = request.POST.get('email')
    request.session['username'] = email
    if email == None:
        return render(request,'email.html')

        
    print(email)
    otp = ''
    rand = random.choice('0123456789')
    rand1 = random.choice('0123456789')
    rand2 = random.choice('0123456789')
    rand3 = random.choice('0123456789')
    otp = rand + rand1 + rand2 + rand3
    print(otp)
    request.session['otp'] = otp
    
    port = 465
    password = "90540564"
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    server.login("maparauvesh5@gmail.com",password)
    server.sendmail("rushansaiyed5884@gmail.com",email,otp)
    server.quit()
    return redirect('otpcheck')
        

    return render(request,'email.html')

def otpcheck(request):
    if request.session.has_key('otp'):
        otp = request.session['otp']
        try:
            otpobj = request.POST.get('otp')
            if otpobj == None:
                return render(request,'otp.html')
            if otp == request.POST.get('otp'):
                return redirect('newpassword')
            else:
                return HttpResponse("<a href = ''>Wrong OTP Entered.</a>")
        except:
            return redirect('login')
    return render(request,'otp.html')

def newpassword(request):
    new_pass = request.POST.get('password')
    if new_pass == None:
        return render(request,'forgotpassword.html')
    obj = Signup.objects.get(email = request.session['username'])
    obj.password = new_pass
    obj.confirmpassword = new_pass
    obj.save()
    print(obj)
    return redirect('login')

def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
        return redirect('login')

def index(request):
    if request.session.has_key('email'):
        a=Product.objects.all()
        s=request.GET.get('search')
        cat=Category.objects.all()
        if s:
            q=Product.objects.filter(Q(name__icontains=s) | Q(des__icontains=s))
            if not q:
                HttpResponse("<h1>Not Item Available.....</h1>")
        else:
            q=Product.objects.all()
        user=request.session['email']
        print(user)
        per=Signup.objects.get(email=user)
        print(per)
        context={
            'pro':q,
            'cat':cat,
            'per':per
        } 
    else:
        return redirect('login')   
    return render(request,'index.html',context)
    

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
def Book(request):
    if request.session.has_key('otp'):
        x=Table.objects.filter(status =True)
        if request.method == 'POST':
            obj=bookingdate()
            obj.date=request.POST['date']
            obj.save()
    else:
        return redirect('login')
    return render(request,'table_book.html',{'abc':x})

def catewise(request,name):
    cat=Category.objects.get(name=name)
    product=Product.objects.all().filter(categories=cat)

    return render(request,'catwise.html',{'cat':cat,'pro':product})

def productview(request,pk):
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'productview.html', {'p': p})
# def shoplist(request):
#     a=Category.objects.all()
#     b=Product.objects.all()

#     if request.method=="POST":
#         b = Book.objects.all()
#         user= request.session['email']
#         print(user1)
#         per = Signup.objects.get(email=user)
#         return render(request, 'index.html', {'b': b, 'a':a})

#     return render(request, 'index.html', {'b': b,'a':a})

def order(request):
    product=Product.objects.all()
    return render(request,'order.html',{'object_list':product})

def add(request):
    form = editform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order')
    return render(request,'pro_add.html', {'form':form})

def edit(request,pk):
    product= get_object_or_404(Product, pk=pk)
    form = editform(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('order')
    return render(request,'edit.html', {'form':form})

def delete(request, pk):
    product= get_object_or_404(Product, pk=pk)    
    product.delete()
    return redirect('order')

def editprofile(request):
    if request.session.has_key('email'):
        data = Signup.objects.get(email=request.session['email'])
        if request.method == 'POST':
            data.username = request.POST.get('username')
            data.email = request.POST.get('email')
            data.phone = request.POST.get('phone')
            data.save()
            return redirect('login')
    return render(request,'editprofile.html',{'data':data})

def add_to_cart(request,pk):
    if request.session.has_key('email'):
        per = Signup.objects.get(email=request.session['email'])
        p = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            if Mycart.objects.filter(product__id=p.id, user__id=per.id,status=False).exists():
                messages.warning(request, 'This item is already in the cart')
                return render(request, 'productview.html', {'p': p, 'per': per})
            else:
                cart=Mycart()
                cart.user=per
                cart.product=p
                cart.save()
                return redirect('showmycart')
        return render(request, 'shop-cart.html', {'p': p, 'per': per})
    else:
        return redirect('login')
    return render(request,'shop-cart.html')   

def show_mycart(request):
    if request.session.has_key('email'):
        obj = Signup.objects.get(email=request.session['email'])
        all = Mycart.objects.filter(user_id=obj.id)
        l=[]
        p=0
        for i in all:
            l.append(i.product)
            p=p+i.product.price
        print(p)
        return render(request,'shop-cart.html',{'al':l,'all':all,'n':obj,'p':p})
    else:
        return redirect('login')
    return render(request,'shop-cart.html')

def remove_cart(request,id):
    if request.session.has_key('email'):
        obj = Signup.objects.get(email=request.session['email'])
        y = get_object_or_404(Mycart,product=id,user_id=obj.id)
        y.delete()
        return redirect('showmycart')