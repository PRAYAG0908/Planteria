from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    indoorplant = Product.objects.filter(tags__tags__icontains='Indoor-plant')
    floweringplant = Product.objects.filter(tags__tags__icontains='Outdoor-plant')
    largeplant = Product.objects.filter(tags__tags__icontains='large-plant')
    fertilizer = Product.objects.filter(tags__tags__icontains='Fertilizer')
    Gardeningtool = Product.objects.filter(tags__tags__icontains='Gardening-tool')
    context = {
               "indoorplants" : indoorplant,
               "floweringplants": floweringplant,
               "largeplants" : largeplant,
               "fertilizers" : fertilizer,
               "Gardeningtools": Gardeningtool,
               }
    return render(request, 'store.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {"items" : items, "order" : order}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)