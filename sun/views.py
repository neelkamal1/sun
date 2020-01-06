from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def home(request):

    return render(request, 'sun/index.html')



def cont(request):
    return render(request,'sun/cont.html')

def rest(request):
    return render(request,'sun/rest.html')

def banq(request):
    return render(request,'sun/banq.html')

def lawn(request):
    return render(request,'sun/lawn.html')

def room(request):
    return render(request,'sun/room.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request,'sun/signu.html',  {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'sun/index.html', context)
