from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from user_panel.views import _cart_session_id
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from user_panel.models import *
from .models import Admin


def login(request):
    user = request.user
    if user.is_authenticated:
        return redirect('user_home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
                
            try:
                user_obj = User.objects.get(username=username)
            except User.DoesNotExist:
                if user is None:
                    uname_error = 'Invalid creditials ! !'
                    context = {
                        'uname_error':uname_error,
                    }
                    return render(request, 'User/login.html', context)

            block_user_login = user_obj.is_active
            print(user_obj)

            if block_user_login == False:
                block_error = 'This user was blocked'
                context = {'block_error':block_error,}
                return render(request, 'User/login.html', context)
                
            elif user is not None:
                # This try and exception are guest cartItems merge to the user cart
                try:
                    cart = Cart.objects.get(cart_id=_cart_session_id(request))
                    exists = CartItem.objects.filter(cart=cart).exists()
                    if exists:
                        cart_item = CartItem.objects.filter(cart=cart)

                        for ct in cart_item:
                            ct.user = user
                            ct.save()
                except:
                    pass
                
                auth_login(request, user)
                return redirect('user_home') #?next={{request.path}}
         
    return render(request, 'User/login.html')


def signup(request):
    user = request.user
    if user.is_authenticated:
        return redirect('user_home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')
            if password == confirm_password:
                user = User.objects.create_user(username=username, email=email, password=password)
                auth_login(request, user)
                print("user created")
                return redirect('user_home')
            else:
                pword_error = "Password did not match ! !"
                print(pword_error)
                return render(request, 'User/signup.html', {'pword_error':pword_error})

    return render(request, 'User/signup.html')


def logout(request):
    auth_logout(request)
    request.session['admin'] = True
    return redirect('user_home')

# def admin_session(request):
#     if request.session.has_key('admin'):
#         return render(request, 'Admin/dashboard.html')
#     else:
#         return render(request, 'Admin/admin_login.html')

def admin_login(request):
    if request.session.has_key('admin'):
        return render(request, 'Admin/dashboard.html')
    else:

        if request.method == 'POST':

            admin = Admin.objects.get(username='admin', password='admin')

            username = request.POST.get('username')
            password = request.POST.get('password')

            if username == admin.username and password == admin.password:
                print('admin logged in')
                request.session['admin'] = True
                # return JsonResponse({'status': 'ok'});
                return redirect('admin_home')
            else:
                invalid_error = "Invalid creditials ! !"
                print(invalid_error)
                # return JsonResponse({'status': 'login failed'})
                # return redirect('admin_login')
                return render(request, 'Admin/admin_login.html', {'invalid_error':invalid_error})
        else:
            return render(request, 'Admin/admin_login.html')


def admin_logout(request):
    del request.session['admin']
    return redirect('admin_login')