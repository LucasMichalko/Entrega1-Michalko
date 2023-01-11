from django.urls import path

from products.views import list_clothing, list_perfume, list_ring

urlpatterns = [
    path('list_clothing/', list_clothing),
    path('list_perfume/', list_perfume),
    path('list_ring/', list_ring),

]