from django.shortcuts import render,HttpResponse
from app.forms import *


# Create your views here.

def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST, request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            MUFDO= ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            
            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            return HttpResponse('submitted successfully')
        else:
            return HttpResponse('invalid data')
        
    return render(request, 'registration.html',d)
