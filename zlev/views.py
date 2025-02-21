from django.shortcuts import render,HttpResponse

# Create your views here.


    

def home(request):
    print("HOME VIEW: is_authenticated =", request.user.is_authenticated)
    return render(request, 'home.html')

