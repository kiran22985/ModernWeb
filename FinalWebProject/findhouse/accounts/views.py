from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,LoginForm,UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import Profile
# Create your views here.
def registerform(request):
    if request.user.is_authenticated:
        return redirect('/findhouse.com/index')
    else:
        if request.method=='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                Profile.objects.create(user=user, username=user.username)
                messages.add_message(request,messages.SUCCESS, 'User registered successfully. please login to continue')
                return redirect('/login')

            else:
                messages.add_message(request, messages.ERROR, 'please provide correct details')
                return render(request,'accounts/registerPage.html',{'form':form})


    context={
        'form':UserCreationForm(),
    }
    return render(request, 'accounts/registerPage.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/findhouse.com/index')
    else:
        if request.method=="POST":
            form=LoginForm(request.POST)
            if form.is_valid():
                data=form.cleaned_data
                user=authenticate(request,username=data['username'], password=data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/findhouse.com/index')

                else:
                    messages.add_message(request, messages.ERROR, 'invalid password')
                    return render(request, 'accounts/login.html', {'form': form})
    form=LoginForm()
    context={
        'form':form
    }
    return render(request,'accounts/login.html', context)

def registerownerform(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'User registered successfully. please login to continue')
            return redirect('/login')

        else:
            messages.add_message(request, messages.ERROR, 'please provide correct details')
            return render(request,'accounts/registerOwner.html',{'form':form})


    context={
        'form':UserForm(),
    }
    return render(request, 'accounts/registerowner.html', context)

def logout_user(request):
    logout(request)
    return redirect('/findhouse.com/index')



def user_account(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Account update successfully for' +" "+str(request.user.username))
            return redirect('/profile')

    context={'form':form}
    return render(request, 'accounts/profile.html',context)