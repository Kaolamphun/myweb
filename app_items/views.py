from django.shortcuts import render

from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, timedelta
from simple_search import search_filter


from app_items.models import ItemCategory, ItemProduct
from django.core.paginator import Paginator, EmptyPage , InvalidPage


# Create your views here.




def index(request: HttpRequest):
    # ຈຳນວນສິນຄ້າທິສະແດງໃນ 1 ໜ້າ
    itemsPerpage = 6

    categories = ItemCategory.objects.order_by("-id")  # categories
    items = ItemProduct.objects.all().order_by("-id") # items [:6]

    paginator = Paginator(items, itemsPerpage)
    try:
        page = int(request.GET.get('page', '1')) # paginate
    except:
        page = 1

    try:
        item_per_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        item_per_page = paginator.page(Paginator.num_pages)


    context = {
        'categories': categories, 
        'items': item_per_page
    }   # context
    return render(request, "index.html", context)



def single_item(request: HttpRequest, id):
    singleitem = ItemProduct.objects.get(id=id) # .all()
    context = {
        'singleItem': singleitem
    }
    return render(request, "single_item.html", context)


# def serch(request: HttpRequest):
#     search_item = ['name_item', 'category_item']
#     query  = ''
#     posts = ItemProduct.objects.filter(search_filter(search_item, query))
#     context = {
#         'posts' : posts
#     }
#     return render(request, "index.html", context)

def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name_item', None)
        if query_name:
            results = ItemProduct.objects.filter(name_item__contains=query_name)
            return render(request, 'product-search.html', {"results":results})

    return render(request, 'product-search.html')