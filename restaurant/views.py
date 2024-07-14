from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from customer.models import *
# Create your views here.
def Home(request):
    return render(request,'restaurant/home.html')
def Admin_login(request):
    if request.method=='POST':
        REmail = request.POST['email']
        RPassword = request.POST['password']
        try:
            rest=Restaurant_reg.objects.get(restemail=REmail,restpassword=RPassword)
            request.session['restaurant']=rest.id
            return redirect('restaurant:view_restaurant')
        except Restaurant_reg.DoesNotExist:
            return render(request,'restaurant/admin_login.html',{'msg':'invalid email or password'})
    return render(request,'restaurant/admin_login.html')
def Add_restaurant(request):
    if request.method=='POST':
        Rname = request.POST['rname']
        Remail = request.POST['remail']
        Rnumber = request.POST['rnumber']
        Rpassword = request.POST['rconfirm_password']
        Raddress = request.POST['raddress']
        restu=Restaurant_reg(restname=Rname,restemail=Remail,restphone=Rnumber,restpassword=Rpassword,restaddress=Raddress)
        restu.save()
    return render(request,'restaurant/add_restaurant.html')
def View_restaurant(request):
     

    if 'restaurant' in request.session:
        restaurant_id = request.session.get('restaurant')
        rest = Restaurant_reg.objects.get(id=restaurant_id)
        dishes = Dishes.objects.filter(drestaurant=rest)
        context={
            "dishes":dishes,
            "rest":rest
        }


    return render(request,'restaurant/view_restaurant.html',context)
def Logout(request):
    if 'restaurant' in request.session:
        del request.session['restaurant']
        return redirect('restaurant:admin_login')
    else:
        return render(request,'restaurant/home.html')
    
def Add_menu(request):
    if 'restaurant' in request.session:
        restaurant_id = request.session.get('restaurant')
        rest = Restaurant_reg.objects.get(id=restaurant_id)
        if request.method=='POST':
            Dname = request.POST['dname']
            Ddescription = request.POST['ddescription']
            Dprice = request.POST['dprice']
            Dimage = request.FILES['dimage']
            Drest = rest
            dish=Dishes(dname=Dname,ddiscription=Ddescription,dprice=Dprice,dimage=Dimage,drestaurant=Drest)
            dish.save()

        return render(request,'restaurant/add_menu.html')
def View_menu(request):
    if 'restaurant' in request.session:
        restaurant_id = request.session.get('restaurant')
        rest = Restaurant_reg.objects.get(id=restaurant_id)
        dishes = Dishes.objects.filter(drestaurant=rest)
        context={
            "dishes":dishes
        }
        
        return render(request,'restaurant/view_menu.html',context)
def Update(request,dish_id):
    dish_details=Dishes.objects.get(id=dish_id)
    if request.method=='POST':
            Dname = request.POST['dname']
            Ddescription = request.POST['ddescription']
            Dprice = request.POST['dprice']
            try:
              Dimage = request.FILES['dimage']
            except:
             Dimage=dish_details.dimage
           
            dish_details.dname=Dname
            dish_details.ddiscription=Ddescription
            dish_details.dprice=Dprice
            dish_details.dimage=Dimage
            dish_details.save()
    context={
        "dish_details":dish_details
    }


    return render(request,'restaurant/update.html',context)
def Delete(request,dish_id):
    Dishes.objects.get(id=dish_id).delete()
    return redirect('restaurant:view_restaurant')
def edit_restaurant(request,rest_id):
    rest_details=Restaurant_reg.objects.get(id=rest_id)
    if request.method=='POST':
            Rname = request.POST['rname']
            Rphone= request.POST['rnumber']
            Remail = request.POST['remail']
            Raddress = request.POST['raddress']
            Rconfirm = request.POST['rconfirm_password']
             
           
            rest_details.restname=Rname
            rest_details.restphone=Rphone
            rest_details.restemail=Remail
            rest_details.restaddress=Raddress
            rest_details.restpassword=Rconfirm
            rest_details.save()
    context={
        "rest_details":rest_details
    }


    return render(request,'restaurant/edit_restaurant.html',context)
def view_order(request):
    if 'restaurant' in request.session:
        restaurant_id = request.session.get('restaurant')
        restaurant = Restaurant_reg.objects.get(id=restaurant_id)
        orders = Order.objects.all()
        order_details = OrderDetail.objects.filter(restaurant=restaurant)
        context={
            "orders":orders,
            "restaurant":restaurant,
            "order_details":order_details
            
             
        }
        
        # order_details = []

        # for order in orders:
        #     details = OrderDetail.objects.filter(order=order)
        #     order_details.append({
        #         'order':order,
        #         'details':details,
        #         'customer':order.customer

        #     })
        #     context={
        #         'restaurant':restaurant,
        #         'order_details':order_details
        #     }
        return render(request,'restaurant/view_order.html',context)
    else:
            return redirect('restaurant:login')

 