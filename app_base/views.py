from django.shortcuts import render

from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, timedelta

from app_items.models import ItemCategory, ItemProduct


# Create your views here.
def index(request: HttpRequest):
    categories = ItemCategory.objects.order_by("-id")  # categories
    items = ItemProduct.objects.order_by("-id")
    context = {'categories': categories, 'items': items}   # item
    return render(request, "index.html", context)


