from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import Account
from django.contrib import auth



def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Account.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('register')
            
        account = form.save(commit = False)
        account.first_name = form.cleaned_data['first_name']
        account.last_name = form.cleaned_data['last_name']
        account.phone_number = form.cleaned_data['phone_number']
        account.username = email.split('@')[0]

        password = form.cleaned_data['password']
        account.set_password(password)  # Hash the password

        account.save()
        messages.success(request,'Registration successful')
        return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        account = Account.objects.filter(email=email).first()

        if account is not None:
            if account.check_password(password):
                auth.login(request,account)
                print("User authenticated:", request.user.is_authenticated) 
                messages.success(request,'Login successful')
                return redirect('home')
            else:
                print("Incorrect password")
                messages.error(request,'Incorrect password')
        else:
            messages.error(request,'Account does not exist')    

    return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request,'You are logged out')
    return redirect('home')


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             account = form.save(commit=False)
#             # Here, you would normally hash the password:
#             # account.password = hash_function(form.cleaned_data['password'])
#             account.save()
#             return redirect('login')  # Replace 'login' with the name of your login URL
#     else:
#         form = RegistrationForm()
    
#     return render(request, 'accounts/register.html', {'form': form})