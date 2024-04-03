from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class License(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    licence_key = models.CharField(max_length=16)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pcname = models.CharField(max_length=255)
    lic_used = models.IntegerField(default=0)
    lic_active = models.BooleanField(default=False)
    register_date = models.DateTimeField(auto_now_add=True)
    activate_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.email} - {self.licence_key}"

class AdminUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Admin_User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AdminUserManager()  # Use custom user manager

    def __str__(self):
        return self.email