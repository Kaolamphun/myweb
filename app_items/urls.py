from django.urls import path 
from .views import *

urlpatterns = [
    path("search", search_product, name="search"),
    path("", index, name="index"),
    path("item/<int:id>", single_item, name="single_item"),
    
]
