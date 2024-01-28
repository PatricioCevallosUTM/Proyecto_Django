from django.shortcuts import render

def base(request):
    return render(request, "core/base.html")

def sample(request):
    return render(request, "core/sample.html")

def nosotros(request):
    return render (request, "core/nosotros.html")

def articulos(request):
    return render (request, "core/articulos.html")

def contacto(request):
    return render (request, "core/contacto.html")