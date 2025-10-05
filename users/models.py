from pyexpat import model
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin,Group, Permission
from .manager import CustomUserManager
import uuid
from django.utils.text import slugify

ROLE_CHOICES=[
    ('admin', 'Admin'),
    ('user', 'User'),
    ('superadmin','Superadmin')
]

transaction_status_choices=(("Success","Success"),
                 ("In Progress","In Progress"),
                 ("On Hold","On Hold"),
                 ("Failed","Failed"),
                 ("Pending","Pending"),
                 ("Aborted","Aborted"),
                 ("Unconfirmed","Unconfirmed"),
                 ("Cancelled","Cancelled")
                 )


sale_choices=(("Local_Hotel","Inventory Hotel"),
                 ("TripJack_Hotel","TripJack Hotel"),
                 ("Local_Flights","Inventory Flights"),
                 ("TripJack_Flights","TripJack Flights"),
                 )

class CustomUser(AbstractUser):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(('username'), max_length=150, blank=True)
    contact_no = models.BigIntegerField(('contact no'), blank=True, null=True)
    email = models.EmailField(('email address main'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    contact_no = models.BigIntegerField(('contact no'), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default='user')
    last_login=models.DateTimeField(blank=True,null=True)
    is_admin=models.BooleanField(default=False)

    @property
    def is_adminuser(self):
        return hasattr(self,"staff_profile")
    
    @property
    def is_customer(self):
        return hasattr(self,"customer_profile")

    @property
    def is_superadmin(self):
        return self.is_superuser  
    
    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Change this to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
    

class Customer(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE,related_name="customer_profile")
    
    def save(self, *args, **kwargs):

        if hasattr(self.user, "staff_profile"):
            raise ValueError("This user is already a Staff, cannot be a Customer")
        super().save(*args, **kwargs)


class Staff(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE,related_name="staff_profile" )
    is_Registered = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if hasattr(self.user, "customer_profile"):
            raise ValueError("This user is already a Customer, cannot be Staff")
        super().save(*args, **kwargs)


