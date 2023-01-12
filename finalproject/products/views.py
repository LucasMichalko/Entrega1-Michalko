from django.shortcuts import render
from django.http import HttpResponse

from products.models import Clothing, Perfum, Ring

def list_clothing(request):
    all_clothing = Clothing.objects.all()
    context = {
        'clothing':all_clothing
    }
    return render(request , 'list_clothing.html', context=context)

def list_perfume(request):
    all_perfume = Perfum.objects.all()
    context = {
        'perfume':all_perfume
    }
    return render(request , 'list_perfume.html', context=context)

def list_ring(request):
    all_ring = Ring.objects.all()
    context = {
        'ring':all_ring
    }
    return render(request , 'list_ring.html', context=context)

def create_clothing(request):
    if request.method == 'GET':
        return render(request , 'create_clothing.html', context={})
    elif request.method == 'POST':
        Clothing.objects.create(name = request.POST ['name'], colour = request.POST['colour'], size = request.POST['size'], price = request.POST['price'])
        return render(request , 'create_clothing.html', context={})

def create_perfume(request):
    if request.method == 'GET':
        return render(request , 'create_perfume.html', context={})
    elif request.method == 'POST':
        Perfum.objects.create(name = request.POST ['name'], smell = request.POST['smell'], price = request.POST['price'])
        return render(request , 'create_perfume.html', context={})
    

def create_ring(request):
    if request.method == 'GET':
        return render(request , 'create_ring.html', context={})
    elif request.method == 'POST':
        Ring.objects.create(name = request.POST ['name'], material = request.POST['material'], weight = request.POST['weight'], price = request.POST['price'])
        return render(request , 'create_clothing.html', context={})     

# Create your views here.
