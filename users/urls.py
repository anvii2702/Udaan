
from django.urls import path, re_path
from users import views

urlpatterns = [
    path('sign-up/', views.Sign_up, name='sign_up'),
    path('sign-in/', views.Sign_in, name='sign_in'),
    path('logout/',views.logout_view,name='logout'),
    path('forget_password/',views.forgot_Password,name='forget_password'),
    path('reset-password/',views.reset_Password,name='reset_password'),
    path('profile/',views.profile,name='profile'),
    
]