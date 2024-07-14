from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from restaurant.models import *
# Create your views here.
def Index(request):
    rest = Restaurant_reg.objects.all()
    context={
        "rest":rest
    }
    return render(request,'customer/index.html',context)
def Signup(request):
    if request.method=='POST':
        Name = request.POST['name']
        Email = request.POST['email']
        Number = request.POST['number']
        Address = request.POST['address']
        Password = request.POST['confirm_password']
        cust=Customer_registration(name=Name,email=Email,number=Number,address=Address,password=Password)
        cust.save()

    return render(request,'customer/signup.html')
def Login(request):
    if request.method=='POST':
        Email = request.POST['email']
        Password = request.POST['confirm_password']
        try:
            cust=Customer_registration.objects.get(email=Email,password=Password)
            request.session['customer']=cust.id
            
            return redirect('customer:dashboard')
        except Customer_registration.DoesNotExist:
            return render(request,'customer/login.html',{'msg':'invalid email or password'})
         
    return render(request,'customer/login.html')
def Dashboard(request):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cust = Customer_registration.objects.get(id=customer_id)
        rest = Restaurant_reg.objects.all()
        context={
            "cust":cust,
            "rest":rest
        }
        return render(request,'customer/dashboard.html',context)
    else:
        return render(request,'customer/index.html')
def Logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return redirect('customer:index')
    else:
        return render(request,'customer/index.html')
def search(request):
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            dishes=Dishes.objects.filter(ddiscription__icontains=keyword)
            context={
                "dishes":dishes
            }
    return render(request,'customer/view_rest.html',context)
def View_rest(request):
    if 'customer' in request.session:
     dishes=Dishes.objects.all()
     
     context={
         "dishes":dishes
     }
     return render(request,'customer/view_rest.html',context)
    else:
        return render(request,'customer/login.html')
    
def menu(request):
    if 'customer' in request.session:
     dishes=Dishes.objects.all()
     context={
         "dishes":dishes
     }
     return render(request,'customer/view_rest.html',context)
    else:
       dishes=Dishes.objects.all()
       context={
         "dishes":dishes
     }
    return render(request,'customer/view_menu.html',context)
def View_menu(request):
    if 'customer' not in request.session:
     dishes=Dishes.objects.all()
     
     context={
         "dishes":dishes
     }
     return render(request,'customer/view_menu.html',context)
    else:
        return render(request,'customer/view_rest.html')
     
def add_to_cart(request,product_id):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
         
        cust = Customer_registration.objects.get(id=customer_id)
        if request.method=='POST':
            dish = Dishes.objects.get(id=product_id)
            rest = dish.drestaurant
            
            cart_item,created=Cart.objects.get_or_create(dish=dish,customer=cust,restaurant=rest)
            
            
            if not created:
                cart_item.quantity+=1
                cart_item.save()
        return redirect('customer:cart')
    else:
        return redirect('customer:login')





def restaurants(request,category):
    
    if category=="pizza":
        dishes=Dishes.objects.filter(ddiscription__icontains=category)
        context={
                "dishes":dishes
            }
    elif category=="dosa":
        dishes=Dishes.objects.filter(ddiscription__icontains=category)
        context={
                "dishes":dishes
            }
    elif category=="burger":
        dishes=Dishes.objects.filter(ddiscription__icontains=category)
        context={
                "dishes":dishes
            }
    elif category=="cake":
        dishes=Dishes.objects.filter(ddiscription__icontains=category)
        context={
                "dishes":dishes
            }
    elif category=="biriyani":
        dishes=Dishes.objects.filter(ddiscription__icontains=category)
        context={
                "dishes":dishes
            }
    elif category=="sandwich":
        dishes=Dishes.objects.filter(ddiscription__icontains=category)
        context={
                "dishes":dishes
            }

    return render(request,'customer/restaurants.html',context)
def index_restaurant(request,rest_id):
        resta =Restaurant_reg.objects.get(id=rest_id)
        dishes = Dishes.objects.filter(drestaurant=resta)
        rest = Restaurant_reg.objects.all()
   
        context = {
            "resta":resta,
            "dishes":dishes,
            "rest":rest

        }

    
        return render(request,'customer/index_restaurant.html',context)
def cart(request):
    
    if 'customer'in request.session:
        customer_id=request.session.get('customer')
        cust = Customer_registration.objects.get(id=customer_id)
        cart_items=Cart.objects.filter(customer=cust)
        
        

        total_price = sum(item.dish.dprice*item.quantity for item in cart_items)
        context={
            "total_price":total_price,
            "cart_items":cart_items,
            "cust":cust
        }
    return render(request,'customer/cart.html',context)
def remove_from_cart(request,item_id):
    if 'customer'in request.session:
        customer_id=request.session.get('customer')
        cust = Customer_registration.objects.get(id=customer_id)
        dish = Dishes.objects.get(id=item_id)
        cart_item = Cart.objects.get(dish=dish,customer=cust)
        cart_item.delete()
        return redirect('customer:cart')
def Buy_now(request):
     
    if 'customer'in request.session:
        customer_id=request.session.get('customer')
        cust = Customer_registration.objects.get(id=customer_id)
        cart_items = Cart.objects.filter(customer=cust)
 
        if not cart_items.exists():
            return redirect('customer:cart')
        restaurant = cart_items.first().restaurant
        total_price = sum(item.dish.dprice*item.quantity for item in cart_items)
        order = Order.objects.create(customer = cust,total_price = total_price,status = 'Pending',restaurant_detail=restaurant)
        for item in cart_items:
            OrderDetail.objects.create(order=order,dish=item.dish,quantity=item.quantity,restaurant=item.restaurant)
        cart_items.delete()
        order_details=OrderDetail.objects.filter(order=order)
        context={
            "cust":cust,
            "order":order,
            "total_price":total_price,
            "order_details":order_details
        }
         
        return render(request,'customer/payment.html',context)
    else:
        return render(request,'customer/index.html')
    

def add_to_cart2(request,dish_id):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
         
        cust = Customer_registration.objects.get(id=customer_id)
        if request.method=='POST':
            dish = Dishes.objects.get(id=dish_id)
            cart_item,created=Cart.objects.get_or_create(dish=dish,customer=cust)
            
            
            if not created:
                cart_item.quantity+=1
                cart_item.save()
        return redirect('customer:cart')
    else:
        return redirect('customer:login')


 