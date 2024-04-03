from django.contrib import admin
from .models import Product, License, Admin_User
# Register your models here.
admin.site.register(Product)
admin.site.register(License)
admin.site.register(Admin_User)