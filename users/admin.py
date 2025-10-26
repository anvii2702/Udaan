from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import AdminSite

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','is_staff','is_active' ,'balance',"role","is_admin","is_customer")
    list_filter = ('email','is_staff','is_active' ,'balance','is_admin','is_customer')
    readonly_fields = ('balance',)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Permission',{'fields':('is_staff','is_active' ,'balance')}),
    )
    add_fieldsets = (
        (None,{'classes':('wide',),
               'fields':('email','password1','password2','is_staff','is_active' ,'balance','is_admin','is_customer')}),
        
    )
    search_fields = ('email',)
    ordering = ('email',)

    
   
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Admin)
admin.site.register(Customer)






class JournalAdmin(admin.ModelAdmin):
    list_display = ("From", "To", "Transaction_id", "agent_balance","Transaction_date","Transaction_amount","Transaction_status","Transaction_remark")
    list_filter = ("From", "To", "Transaction_id", "agent_balance","Transaction_date","Transaction_amount","Transaction_status","Transaction_remark")
    readonly_fields = ("From", "To", "Transaction_id", "agent_balance","Transaction_date","Transaction_amount","Transaction_status","Transaction_remark")

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
