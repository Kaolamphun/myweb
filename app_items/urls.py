from django.urls import path 
from .views import index, single_item

urlpatterns = [

    path("", index, name="index"),
    path("item/<int:id>", single_item, name="single_item"),
    
]
