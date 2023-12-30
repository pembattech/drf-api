from django.urls import path

from .views import *

urlpatterns = [
    path('', drink_list, name = 'drink_list' ),
    path('drink_detail/<int:id>', drink_detial, name = "drink_detail"),
]
