from django.shortcuts import render,HttpResponse,redirect
import zipcode
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth import login

def index(request):
    print request.user
    print request.user.profile.postal_code
    return HttpResponse('sb')

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            uf=user_form.save(commit=False)
            uf.set_password(uf.password)
            uf.save()
            pf=profile_form.save(commit=False)
            pf.user=uf
            pf.save()
            login(request,uf)
            return redirect('/')
        else:
            if request.is_ajax(): 
                return JsonResponse({'success' : False, 'user_errors' : user_form.errors,'zip':profile_form.errors})
            else:
                messages.error(request, 'Please correct the error below.')
                return redirect('/accounts/signup')
            
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'user/regit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def show(request):
    user=request.user
    return render(request,'user/user_info.html',{'user':user})