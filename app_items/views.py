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



def index(request: HttpRequest):
    categories = ItemCategory.objects.order_by("-id")  # categories
    item = page_item(request)  # items
    # context
    context = {
        'categories': categories, 
        'items': item
    }  
    return render(request, "index.html", context)



def single_item(request: HttpRequest, id):
    singleitem = ItemProduct.objects.get(id=id) 
    context = {
        'singleItem': singleitem
    }
    return render(request, "single_item.html", context)




def search_product(request: HttpRequest):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name_item', None)
        if query_name:
            results = ItemProduct.objects.filter(name_item__contains=query_name)
            return render(request, 'product-search.html', {"items":results})

    return render(request, 'product-search.html')

# def category_filter(request: HttpRequest, category): 
#     categories  =  ItemProduct.objects.all().order_by("-id")
#     for category in categories:

#         filter = ItemProduct.objects.filter(category_item=category.pk)

#         context = {
#             'filter': filter
#         }
#         print(filter)
#     return render(request, 'category.html', context)


def category_filter(request: HttpRequest, categories):
    categories = ItemProduct.objects.all()
    

    filter = ItemProduct.objects.filter(category_item=22)

    context = {
        'filter': filter
    }
    # print(filter)
    return render(request, 'category.html', context)
