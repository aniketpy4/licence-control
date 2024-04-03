from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from .models import Product, License, Admin_User

# Create your views here.
def default(request):
    print("index called")
    if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            purchase_code = request.POST.get('purchase_code')
            product_id = request.POST.get('product_id')
            licence_count = request.POST.get('licence_count')
            licence_expiry = request.POST.get('licence_expiry')
            
            # Assuming product_id is the ID of the selected product
            product = Product.objects.get(pk=product_id)
            
            # Create License object
            license = License.objects.create(
                email=email,
                licence_key=purchase_code,
                product=product,
                lic_used=licence_count,
                expiry_date=licence_expiry
            )
            license.save()
            messages.success(request, 'License added successfully.')
            return redirect('index')
        
        # If GET request, render the index template with product data
        products = Product.objects.all()
        licenses = License.objects.all()  # Fetch all licenses
        return render(request, 'index.html', {'products': products, 'licenses': licenses})
    else:
        return redirect('login')

def login_user(request):
    print("login called")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print("Invalid email or password.")
                messages.error(request, 'Invalid email or password.')
                return redirect('login')
        except Admin_User.DoesNotExist:
            print("Invalid email or password. from except")
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
    # If user is already logged in, redirect to index
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'signin.html', {})

def delete_license(request):
    if request.method == 'POST':
        license_id = request.POST.get('license_id')
        try:
            license = License.objects.get(pk=license_id)
            license.delete()
            messages.success(request, 'License deleted successfully.')
        except License.DoesNotExist:
            messages.error(request, 'License does not exist.')
    return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('login')

def error404(request):
    print("404 called")
    return render(request, '404.html',{})