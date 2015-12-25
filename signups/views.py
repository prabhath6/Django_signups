from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.
def home(request):

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'form': form}
    return render(request, 'signup.html', context)

def thankyou(request):
    context = {}
    return render(request, "thank-you.html", context)


def aboutus(request):
    context = {}
    return render(request, "about-us.html", context)

# def name(request):
#
#     form = Name(request.POST or None)
#     if form.is_valid():
#         save_it = form.save(commit=False)
#         save_it.save()
#
#     context = {'form': form}
#     return render(request, 'name.html', context)