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
    items_per_page = int(9)

    categories = ItemCategory.objects.order_by("-id")  # categories
    items = ItemProduct.objects.all().order_by("-id")[:items_per_page] # items

    paginator = Paginator(items, items_per_page)
    try:
        page = int(request.GET.get('page', '1')) # paginate
    except:
        page = 1

    try:
        itemsPerPage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        itemsPerPage = paginator.page(Paginator.num_pages)


    context = {'categories': categories, 'items': itemsPerPage}   # context
    return render(request, "index.html", context)


