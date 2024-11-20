from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm( )
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"hey{username},your account was created")
            new_user= authenticate(username= form.cleaned_data['email'],
                                   password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("farmcityeccomerce:home.html")

    else:
        print("user cannot be")
        form = UserRegisterForm()

    context= {
        'form': form,
    }

    return render(request,"userauths/signup.html")
