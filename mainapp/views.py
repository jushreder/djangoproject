from django.shortcuts import render
from django.conf import settings
from django.utils import timezone

from mainapp.models import Contact, ProductCategory, Product, Product_option
from basketapp.models import Basket
from django.shortcuts import get_object_or_404

import random

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
                                    exclude(pk=hot_product.pk)[:3]

    return same_products

def main(request, pk='Featured'):
    title = "hOME"
    exclusive_products = Product.objects.filter(short_desc__endswith = 'exclusive')
    trending_products =  Product.objects.filter(short_desc__endswith = 'trending')
    featured_products = Product.objects.all()[:4]
    basket = get_basket(request.user)

    content = {"title": title, 
               "featured_products": featured_products,
               "exclusive_products" : exclusive_products,
               "trending_products" : trending_products,
               "basket" : basket
               }

    
    return render(request, "mainapp/index.html", content)



def products(request, pk=None):
    title = "pRODUCTS"
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
    
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
               "basket" : basket,               
               }
            return render(request, "mainapp/products_list.html", content)
   
    products = Product.objects.all()

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    product_option = Product_option.objects.filter(product_id = hot_product.id)
    content = {"title": title,
               "links_menu": links_menu,
               "hot_product": hot_product,
               "same_products" : same_products,
               "basket" : basket,
               "product_option" : product_option
              }

    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "cONTACTS"
    locations = Contact.objects.all()
    vizit_date = timezone.now()
    basket = get_basket(request.user)

    content = {"title": title,
               "locations": locations,
               "vizit_date": vizit_date,
               "basket" : basket,
               }
               
    return render(request, "mainapp/contact.html", content)

def product(request, pk):
    title = 'продукты'
    product_option = Product_option.objects.filter(product_id=pk)
    content = {
        'title': title, 
        'links_menu': ProductCategory.objects.all(), 
        'product': get_object_or_404(Product, pk=pk), 
        'basket': get_basket(request.user),
        "product_option" : product_option
    }
	

    return render(request, 'mainapp/product.html', content)

