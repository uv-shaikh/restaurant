from django.urls import path
from .views import login,index,register,forgot_pass,otpcheck,newpassword,logout,Book,catewise,productview,add_to_cart,order,edit,delete,add,editprofile,show_mycart,remove_cart,checkout,success

urlpatterns= [
    path('',login,name="login"), 
    path('register/',register,name="register"),
    path('forgotpass/',forgot_pass,name = 'forgotpass'),
    path('logout/',logout,name = 'logout'),
    path('otpcheck/',otpcheck, name = 'otpcheck'),
    path('newpassword/',newpassword, name = 'newpassword'),
    path('index/',index,name="index"),
    path('catwise/<str:name>/',catewise,name="catewise"),
    path('productview/<int:pk>/',productview,name="productview"),
    path('addtocart/<int:pk>/',add_to_cart,name="addtocart"),
    path('order/',order,name="order"), 
    path('create/',add,name="add"), 
    path('proedit/<int:pk>/',edit,name="edit"),
    path('delete/<int:pk>/',delete,name="delete"), 
    path('Table/',Book,name="book"), 
    path('editprofile/',editprofile,name="editprofile"),
    path('showmycart/',show_mycart,name="showmycart"),
    path('deleteitem/<int:id>/',remove_cart, name='deleteitem'),
    path('checkout/',checkout, name='checkout'),
    path('success/',success, name='success')
]