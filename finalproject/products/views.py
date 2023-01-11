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
        'Ring':all_ring
    }
    return render(request , 'list_ring.html', context=context)

# Create your views here.
