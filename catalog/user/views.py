from django.shortcuts import render,redirect

# Create your views here.


def login(request):
    return render(request,'user/login.html')


def register(request):
    if request.method=='POST':
        print('submitted')
        return redirect('register')
    else:
        return render(request,'user/register.html')


def logout(request):
    return render(request,'user/logout.html')



