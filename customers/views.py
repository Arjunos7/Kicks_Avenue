from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if p == cp:
            User.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e)
            return redirect('products:index')
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
    return render(request, 'register.html')

# login with email
def user_login(request):
    if request.method == "POST":
        e = request.POST['e']
        p = request.POST['p']

        try:
            user = User.objects.get(email=e)
        except User.DoesNotExist:
            user = None

        if user is not None:
            user = authenticate(username=user.username, password=p)
            if user is not None:
                login(request, user)
                return redirect('products:index')
            else:
                messages.error(request, 'Invalid password.')
        else:
            messages.error(request, 'Invalid email address.')

        return render(request, 'login.html')

    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('customers:login')