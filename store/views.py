from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        indoorplant = Product.objects.filter(tags__tags__icontains='Indoor-plant')
        floweringplant = Product.objects.filter(tags__tags__icontains='Outdoor-plant')
        largeplant = Product.objects.filter(tags__tags__icontains='large-plant')
        fertilizer = Product.objects.filter(tags__tags__icontains='Fertilizer')
        Gardeningtool = Product.objects.filter(tags__tags__icontains='Gardening-tool')
        
        cartitems = order.get_cart_quantity
        
        context = {
                "indoorplants" : indoorplant,
                "floweringplants": floweringplant,
                "largeplants" : largeplant,
                "fertilizers" : fertilizer,
                "Gardeningtools": Gardeningtool,
                "cartitems":cartitems
                }
        return render(request, 'store.html', context)
    else:
        items = []
        return render(request, 'store.html')
    # return render(request, 'store.html', context)

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
        return render(request, 'cart.html')
    context = {"items" : items, "order" : order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        return render(request, 'checkout.html')
    context = {"items" : items, "order" : order}
    return render(request, 'checkout.html', context)

def UpdateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action', action)
    print('productId', productId)

    customer = request.user.customer
    product = Product.objects.get(pk=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product = product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False) 