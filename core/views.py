from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin_page(request):
    return render(request, 'admin.html')

def galeria(request):
    return render(request, 'galeria.html')

def guardaparamo(request):
    return render(request, 'guardaparamo.html')

def login_page(request):
    return render(request, 'login.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def recuperar_contraseña(request):
    return render(request, 'recuperar_contrasena.html')
