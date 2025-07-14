
from django.urls import path, re_path
from users import views

urlpatterns = [

    path('login/',views.Login__,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('signup/',views.Signup,name='signup'),
    path('forget_password/',views.Forgot_Password,name='forget_password'),
    path('reset_password/',views.Reset_Password,name='reset_password'),
    
]  # End of urlpatterns