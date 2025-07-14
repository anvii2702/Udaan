from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','is_staff','is_active' ,'balance')
    list_filter = ('email','is_staff','is_active' ,'balance')
    readonly_fields = ('balance',)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Permission',{'fields':('is_staff','is_active' ,'balance')}),
    )
    add_fieldsets = (
        (None,{'classes':('wide',),
               'fields':('email','password1','password2','is_staff','is_active' ,'balance')}),
        
    )
    search_fields = ('email',)
    ordering = ('email',)


   
admin.site.register(CustomUser,CustomUserAdmin),
admin.site.register(Staff),
admin.site.register(ammendment)





class JournalAdmin(admin.ModelAdmin):
    list_display = ("From", "To", "Transaction_id", "agent_balance","Transaction_date","Transaction_amount","Transaction_status","Transaction_remark")
    list_filter = ("From", "To", "Transaction_id", "agent_balance","Transaction_date","Transaction_amount","Transaction_status","Transaction_remark")
    readonly_fields = ("From", "To", "Transaction_id", "agent_balance","Transaction_date","Transaction_amount","Transaction_status","Transaction_remark")

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
