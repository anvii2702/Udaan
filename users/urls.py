
from django.urls import path, re_path
from users import views

urlpatterns = [
    path('sign-up/', views.Sign_up, name='sign_up'),
    path('sign-in/', views.Sign_in, name='sign_in'),
    path('login/',views.Login__,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('forget_password/',views.Forgot_Password,name='forget_password'),
    path('reset_password/',views.Reset_Password,name='reset_password'),
    
]  # End of urlpatterns