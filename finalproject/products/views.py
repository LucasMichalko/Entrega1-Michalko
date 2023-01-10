from django.shortcuts import render
from django.http import HttpResponse

from products.models import Clothing

def list_clothing(request):
    all_clothing = Clothing.objects.all()
    context = {
        'clothing':all_clothing
    }
    return render(request , 'list_clothing.html', context=context)

# Create your views here.
