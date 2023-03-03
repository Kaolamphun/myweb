from django.shortcuts import render

# Create your views here.

def single_item(request):
    return render(request, 'single_item.html')