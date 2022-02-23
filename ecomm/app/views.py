
from distutils.command.upload import upload
from django.http import HttpResponse, request
from django.shortcuts import render,redirect


from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from .models import register, product,Category,order
def index(request):
    if request.method == "POST":
        productid = request.POST.get('cartid')
        remove = request.POST.get('minus')

        cartid = request.session.get('cart')
        
        if cartid:
            quantity = cartid.get(productid)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cartid.pop(productid)
                    else:
                        cartid[productid] = quantity - 1
                else:
                    cartid[productid] = quantity + 1            
                
            else:
                cartid[productid] = 1
        else:
            cartid = {}
            cartid[productid] = 1
        request.session['cart'] = cartid
        print(request.session['cart'])        

    path = product.objects.all()
    cat = Category.objects.all()

    catid = request.GET.get('Category')
    if catid:
        path = product.objects.filter(Category_id = catid)
    else:
        path = product.objects.all()
    
    return render(request,'home.html',{'path':path,'cate':cat})

    
def contact(request):
    return render(request,'contact.html')
    
def aboutus(request):
    return render(request,'aboutus.html')    

def save(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')    
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        save_info = register(firstname= fname, lastname= lname,mobile=mobile,password=password,gender=gender,email=email)
        save_info.save()
        return redirect('home')

def register_info(request):
            if request.method == "POST":
                fname = request.POST.get('firstname')
                lname = request.POST.get('lastname')
                mobile = request.POST.get('mobile')
                gender = request.POST.get('gender')
                email = request.POST.get('email')
                password = request.POST.get('password')

                store_data = register(firstname = fname,lastname = lname,mobile = mobile,gender = gender,email = email,password = make_password(password))

                store_data.save()

                return redirect('home')   

def login(request):
    error_msg = None
 
    if request.method == "POST":
        email = request.POST.get('email')

        password = request.POST.get('password') 
    try:
        fetch_email = register.objects.get(email=email)
        if(fetch_email.email == email):
            Flag = check_password(password,fetch_email.password)
            if Flag:
                request.session['email'] = fetch_email.email
                request.session['customer_id'] = fetch_email.id
                return redirect('home')
            else:
                error_msg = "plz enter valid password" 
                return render(request,'home.html',{'error_msg': error_msg}) 
    except:
        error_msg = "please enter valid email"
        return render(request,'home.html',{'error_msg': error_msg})              

        return HttpResponse(fetch_email)

def logout(request):
    request.session.clear()
    return redirect('home')

def cart(request):
    x = list(request.session.get('cart').keys())
    cart = product.objects.filter(id__in = x)
    print(cart)
    return render(request,'cart.html',{'cart_pro':cart}) 

def checkout(request):
    if request.method == "POST":
        address = request.POST.get("address")
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = product.objects.filter(id__in=list(cart.keys()))
    
        for pro in products:
            save_order_dtls = order(
            customer = register(id=customer_id),
            product = pro,
            price = pro.price,
            quantity = cart.get(str(pro.id)),
            address = address,
            phone = mobile)
        
        save_order_dtls.save()    
        request.session['cart'] = {}    

    return redirect('cart')
    

def order_dtls(request):
    customer = request.session.get('customer_id')
    order_dtls = order.objects.filter(customer=customer).order_by('-date')
    tp = 0 
    for i in order_dtls:
        tp = tp+(i.price * i.quantity)
    return render(request,'order.html', {'order_dtls':order_dtls,'tp':tp})
