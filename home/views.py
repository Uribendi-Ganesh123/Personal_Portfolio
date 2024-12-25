from django.shortcuts import render

# Create your views here.

def main1(request):
    return render(request,"home.html")

def main2(request):
    return render(request,"about.html")

def main3(request):
    return render(request,"services.html")

def main4(request):
    return render(request,"portfolio.html")

def main5(request):
    return render(request,"contact.html")