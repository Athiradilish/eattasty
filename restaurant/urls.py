from django.urls import path
from . import views
app_name='restaurant'
urlpatterns=[
    path('home/',views.Home,name='home'),
    path('admin_login/',views.Admin_login,name='admin_login'),
    path('add_restaurant/',views.Add_restaurant,name='add_restaurant'),
    path('view_restaurant/',views.View_restaurant,name='view_restaurant'),
    path('logout/',views.Logout,name='logout'),
    path('add_menu/',views.Add_menu,name='add_menu'),
    path('view_menu/',views.View_menu,name='view_menu'),
    path('update/<int:dish_id>',views.Update,name='update'),
    path('delete_dish/<int:dish_id>',views.Delete,name='delete_dish'),
    path('edit_restaurant<int:rest_id>',views.edit_restaurant,name='edit_restaurant'),
    path('view_order',views.view_order,name='view_order')

 ]