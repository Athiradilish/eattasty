from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('',views.Index,name='index'),
    path('signup/',views.Signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('logout/',views.Logout,name='logout'),
    path('view_rest/',views.View_rest,name='view_rest'),
    path('menu/',views.menu,name='menu'),
    path('restaurants/<str:category>',views.restaurants,name='restaurants'),
    path('search/',views.search,name='search'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('index_restaurant/<int:rest_id>',views.index_restaurant,name='index_restaurant'),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart/<int:item_id>',views.remove_from_cart,name='remove_from_cart'),
    path('buy_now/',views.Buy_now,name='buy_now'),
    path('view_menu/',views.View_menu,name='view_menu'),
    path('add_to_cart2/<int:dish_id>',views.add_to_cart2,name='add_to_cart2')


]