from django.shortcuts import render,HttpResponse

# Create your views here.

def home (request):
    return render(request,'FioramantiWebApp/home.html')

def servicios (request):
    return render(request,'FioramantiWebApp/servicios.html')

def blog (request):
    return render(request,'FioramantiWebApp/blog.html')

def contacto (request):
    return render(request,'FioramantiWebApp/contacto.html')

