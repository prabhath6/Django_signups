from django.shortcuts import render, render_to_response
from .forms import SignUpForm, CreateLoginForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

        # send mail
        # send_main(subject, message, from_mail, to_list, fail_silently=True)
        subject = "Thank you for registering."
        message = "Your account has been registered. Now you can login."
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email]
        #send_mail(subject, message, from_email, to_list)
        return thankyou(request)

    context = {'form': form}
    return render(request, 'signup.html', context)


def auth_view(request):
    user_name = request.POST.get('inputEmail')
    user_password = request.POST.get('inputPassword')
    user = auth.authenticate(username=user_name, password=user_password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedIn')
    else:
        return HttpResponseRedirect('/home')


def createlogin(request):
    form = CreateLoginForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect("/thank-you")

    context = {'form': form}
    return render(request, 'createlogin.html', context)


def thankyou(request):
    context = {}
    return render(request, "thank-you.html", context)


def aboutus(request):
    context = {}
    return render(request, "about-us.html", context)


def login(request):
    context = {}
    return render(request, "login.html", context)


@login_required(login_url='login.html')
def loggedIn(request):
    context = {}
    return render(request, "loggedIn.html", context)


# def name(request):
#
#     form = Name(request.POST or None)
#     if form.is_valid():
#         save_it = form.save(commit=False)
#         save_it.save()
#
#     context = {'form': form}
#     return render(request, 'name.html', context)
