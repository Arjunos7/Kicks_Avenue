from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator


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


def password_reset_request(request):
    if request.method == "POST":
        email = request.POST['email']
        associated_users = User.objects.filter(email=email)
        if associated_users.exists():
            for user in associated_users:
                subject = "Password Reset Requested"
                email_template_name = "registration/password_reset_email.html"
                c = {
                    "email": user.email,
                    'domain': request.META['HTTP_HOST'],
                    'site_name': 'Your Site',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                send_mail(subject, email, 'admin@yourwebsite.com', [user.email], fail_silently=False)
        return redirect('password_reset_done')
    return render(request, 'registration/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

def password_reset_confirm(request, uidb64=None, token=None):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            new_password = request.POST['new_password']
            user.set_password(new_password)
            user.save()
            return redirect('password_reset_complete')
        else:
            return render(request, 'registration/password_reset_confirm.html', {'validlink': True})
    else:
        return render(request, 'registration/password_reset_confirm.html', {'validlink': False})

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')