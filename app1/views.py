from django.shortcuts import render

# Create your views here.
def app1_fun(request):
    return render(request,'app1/app1_fun.html')