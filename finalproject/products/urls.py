from django.urls import path

from products.views import list_clothing

urlpatterns = [
    path('list_clothing/', list_clothing)

]