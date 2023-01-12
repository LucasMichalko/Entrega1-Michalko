from django.urls import path

from products.views import list_clothing, list_perfume, list_ring, create_clothing, create_perfume, create_ring

urlpatterns = [
    path('list_clothing/', list_clothing),
    path('list_perfume/', list_perfume),
    path('list_ring/', list_ring),
    path('create_clothing/', create_clothing),
    path('create_perfume/', create_perfume),
    path('create_ring/', create_ring),

]