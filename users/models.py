

from pyexpat import model
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin,Group, Permission



from .manager import CustomUserManager
from uuid import uuid4
import os
from django.utils.text import slugify


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

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(('username'),unique=True,null=True)
    email = models.EmailField(('email address main'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    contact_no = models.BigIntegerField(('contact no'), blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    
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
    
    @property
    def id(self):
        return int(self.pk)

    pass

class Master(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)


    # Add fields specific to agents
    # Add more agent-specific fields here


class Staff(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    is_Registered = models.BooleanField(default=False)
    Staff_code = models.CharField(max_length=10)

class ammendment(models.Model):
    user_name = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_name")
    slug = models.SlugField(unique=True, blank=True, null=True)
    problem = models.CharField(max_length=250,null=True)
    problem_for = models.CharField(max_length=250,null=True)
    booking_id = models.CharField(max_length=250,null=True)
    query_status = models.BooleanField(default=True)    
    chat = models.JSONField(null=True)
    staff_name = models.ForeignKey(CustomUser,on_delete = models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(null=True)
    
    def _get_unique_slug(self):
            slug = slugify("TRPN-AMD" + str(random.randint(0000,9999))) 
            unique_slug = slug
            num = 1
            while ammendment.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(slug, num)
                num += 1
            return unique_slug
    
    def     save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
        
    
