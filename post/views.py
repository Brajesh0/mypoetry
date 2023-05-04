from django.shortcuts import render, redirect,HttpResponse
from .forms import RagistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,"index.html")


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,username=cd["username"],password=cd["password1"])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("home")
                else:
                    # return HttpResponse("Disable account")
                    messages.error(request, "Disable account")
                    # return redirect("/")
                    
            else:
                messages.error(request, "invalid login")
                # return redirect("/")
                
    else:
        login_form = LoginForm()

    return render(request, 'login.html',{"login_form":login_form})

def signout_user(request):
    if request.method == "POST":
        form = RagistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('user create successfully')
        return redirect('/')
    else:
        form =RagistrationForm()    

    return render(request,'ragistration.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return redirect("/")


#userprofile view
def user_profile(request):
    return render(request,'profile.html')

