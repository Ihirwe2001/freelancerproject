from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreationForm, Contactform

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registration successful')

            return redirect('login')

    context = {
        'form': form,
    }
    return render(request,'register.html', context)

def user_login(request):
    form = UserCreationForm()

    if request.user.is_authenticated:
        messages.warning(request, "Hey, You're already logged in")
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use authenticate with email field
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You're now logged in")
            return redirect('/Business')
        else:
            messages.warning(request, "Invalid username or password. Create an account if you don't have one.")

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "You're logged out")
    return redirect("login")

def contact(request):
    if request.method == "POST":
        form = Contactform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully')
    
    return render(request,'contact.html')

def Business(request):
    return render(request,'Business.html') 

def freelance(request):
    return render(request,'freelance.html')

def free1(request):
    return render(request,'free1.html') 

def free2(request):
    return render(request,'free2.html')

def free3(request):
    return render(request,'free3.html')

def free4(request):
    return render(request,'free4.html')

def free5(request):
    return render(request,'free5.html')

def free6(request):
    return render(request,'free6.html')

def free7(request):
    return render(request,'free7.html')

def free8(request):
    return render(request,'free8.html')

def free9(request):
    return render(request,'free9.html')

def graphic(request):
    return render(request,'graphic.html')

def back(request):
    return render(request,'back.html') 

def analyst(request):
    return render(request,'analyst.html')

def frontend(request):
    return render(request,'frontend.html') 

def reg2(request):
    return render(request,'reg2.html')

def freelreg(request):
    return render(request,'freelreg.html')

def customer(request):
    return render(request,'customer.html')

def partener(request):
    return render(request,'partener.html')        
       


 

