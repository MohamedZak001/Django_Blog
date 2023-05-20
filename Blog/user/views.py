from django.shortcuts import render, redirect
from .forms import Reg,update_user,update_profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def Register(request):
    if request.method == 'POST':
        form = Reg(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {name}")
            return redirect('blog-home')
    else:
        form = Reg()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):

    if request.method == 'POST':
        user_form = update_user(request.POST,instance=request.user)
        profile_form = update_profile(request.POST,request.FILES,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Account has been Updated for ")
            return redirect('blog-home') 
    
    user_form = update_user(instance=request.user)
    profile_form = update_profile(instance=request.user.profile)
    contx = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'profile.html',contx)
