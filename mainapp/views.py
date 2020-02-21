from django.shortcuts import render
from django.conf import settings
from django.utils import timezone

from mainapp.models import Contact, ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404

# import json
# def getProduct(name_file):
#     json_data = open(name_file)
#     product_list = json.load(json_data)
#     json_data.close()
#     return product_list


# Create your views here.

def getBasket(user_is):
    total_amount = 0
    total_cost = 0    
    if user_is.is_authenticated:
        basket = Basket.objects.filter(user=user_is)        
        for product_basket in basket:
            total_amount += product_basket.quantity
            total_cost += Product.objects.get(pk=product_basket.product_id).price * product_basket.quantity       
    return [total_amount, total_cost]


def main(request):
    title = "hOME"
    featured_products = Product.objects.all()[:4]
    # total_amount = 0
    # total_cost = 0
    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)
        
    #     for product_basket in basket:
    #         total_amount += product_basket.quantity
    #         total_cost += Product.objects.get(pk=product_basket.product_id).price * product_basket.quantity

    # content = {"title": title, "featured_products": featured_products, "basket":basket}
    rezult = getBasket(request.user)
    total_amount =rezult[0]
    total_cost = rezult[1]

    content = {"title": title, 
               "featured_products": featured_products,
               "total_amount":total_amount,
               "total_cost":total_cost}

    
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "pRODUCTS"
    links_menu = ProductCategory.objects.all()

    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)

    rezult = getBasket(request.user)
    total_amount =rezult[0]
    total_cost = rezult[1]
    
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {"name": "all"}
        else:
            category = get_object_or_404(ProductCategory, pk = pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

            content = {"title": title, 
               "links_menu": links_menu,
               "products": products,
               "category" : category,
               "total_amount":total_amount,
               "total_cost":total_cost}
            return render(request, "mainapp/products.html", content)


    
    products = Product.objects.all()
    
    content = {"title": title,
               "links_menu": links_menu,
               "products": products,
               "total_amount":total_amount,
               "total_cost":total_cost}

    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "cONTACTS"
    locations = Contact.objects.all()
    vizit_date = timezone.now()
    rezult = getBasket(request.user)
    total_amount =rezult[0]
    total_cost = rezult[1]
    content = {"title": title,
               "locations": locations,
               "vizit_date": vizit_date,
               "total_amount":total_amount,
               "total_cost":total_cost}
               
    return render(request, "mainapp/contact.html", content)


def history(request):
    title = "hISTORY"
    rezult = getBasket(request.user)
    total_amount =rezult[0]
    total_cost = rezult[1]
    content = {"title": title,
               "total_amount":total_amount,
               "total_cost":total_cost}
    return render(request, "mainapp/history.html", content)


def showroom(request, pk=None):
    title = "sHOWROOM"
    links_menu = ProductCategory.objects.all()
    rezult = getBasket(request.user)
    total_amount =rezult[0]
    total_cost = rezult[1]

    content = {"title": title,
               "links_menu": links_menu,
               "total_amount":total_amount,
               "total_cost":total_cost}
 
    return render(request, "mainapp/showroom.html", content)

