from django.shortcuts import get_object_or_404, render

from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, timedelta
from simple_search import search_filter


from app_items.models import ItemCategory, ItemProduct
from django.core.paginator import Paginator, EmptyPage , InvalidPage


# Create your views here.



def page_item(request: HttpRequest):
     # ຈຳນວນສິນຄ້າທີສະແດງໃນ 1 ໜ້າ
    itemsPerpage = 6
    items = ItemProduct.objects.all().order_by("-id") # items [:6]
    paginator = Paginator(items, itemsPerpage)
    try:
        page = int(request.GET.get('page', '1')) # paginate
    except:
        page = 1

    try:
        item = paginator.page(page)
    except (EmptyPage, InvalidPage):
        item = paginator.page(Paginator.num_pages)
    return item



def category(requset: HttpRequest):
    categories = ItemCategory.objects.order_by("pk")
    res = []
    [res.append(i) for i in categories if i not in res]
    return res



def index(request: HttpRequest):
    categories_product = category(request)
    items = page_item(request)  # items
    context = {
        'categories': categories_product, 
        'items': items
    }  
    return render(request, "index.html", context)



def single_item(request: HttpRequest, id):
    singleitem = ItemProduct.objects.get(id=id)
    categories_product = category(request)
    context = {
        'categories': categories_product, 
        'singleItem': singleitem
    }
    return render(request, "single_item.html", context)




def search_product(request: HttpRequest):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name_item', None)
        if query_name:
            results = ItemProduct.objects.filter(name_item__contains=query_name)
            categories_product = category(request)
            context = {
                "items":results,
                "categories":categories_product,
            }
            return render(request, 'product-search.html', context)

    return render(request, 'product-search.html')



def category_filter(request: HttpRequest, categories):
    if request.method == "GET":
        query_name = request.GET.get(str(categories), categories)
        print(query_name)
        filter = ItemProduct.objects.filter(
            category_item__category_item=query_name)
        categories_product = category(request)
        
        context = {
            'categories': categories_product,
            'filter': filter
        }
        return render(request, 'category.html', context)
