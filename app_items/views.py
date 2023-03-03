from django.shortcuts import render

from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, timedelta

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


    context = {'categories': categories, 'items': item_per_page}   # context
    return render(request, "index.html", context)



def single_item(request: HttpRequest, id):
    singleitem = ItemProduct.objects.get(id=id) # .all()
    context = {'singleItem': singleitem}
    return render(request, "single_item.html", context)

