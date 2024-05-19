from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required


# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username'],
#         password = request.POST['password'],
        
#         user = auth.authenticate(username = username, password =password)
       
#         if user is not None:
#             auth.login(request, user)
#             return redirect("/addbus")
#         else:
#             messages.info(request, 'Invalid credentials')
#             return redirect('login')
    
#     else:
#         return render(request, 'login.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)  # Hypothetical password hashing function

    if user is not None:
      auth.login(request, user)
      return redirect("addbus")
    else:
      messages.info(request, 'Invalid credentials')
      return redirect('account/login')

  else:
    return render(request, 'login.html')

@login_required
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    
        if password == confirm_password:
            if User.objects.filter(username=username).exists(): 
                messages.info(request,'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists(): 
                messages.info(request,'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=confirm_password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'Sucessfully User Register')
                return redirect('login')
        else:
              messages.info(request,'Password and Confirm Password not Match')
              return redirect('/accounts/register')
        
    else:
        return render(request, 'register.html')




# @login_required
# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, 'Email already taken')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(
#                     username=username,
#                     password=password,  # Use the password here, not confirm_password
#                     email=email,
#                     first_name=first_name,
#                     last_name=last_name
#                 )
#                 user.save()
#                 messages.success(request, 'Successfully registered user')
#                 return redirect('login')
#         else:
#             messages.error(request, 'Password and confirm password do not match')
#             return redirect('register')

#     return render(request, 'register.html')


def logout(request):
  auth.logout(request)
  return redirect('/')

