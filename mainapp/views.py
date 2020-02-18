from django.shortcuts import render
from django.conf import settings
from django.utils import timezone

from mainapp.models import Contact, ProductCategory, Product

import json


def getProduct(name_file):
    json_data = open(name_file)
    product_list = json.load(json_data)
    json_data.close()
    return product_list


# Create your views here.


def main(request):
    title = "hOME"
    # featured_products = getProduct("static/products.json")
    featured_products = Product.objects.all()[:4]
    content = {"title": title, "featured_products": featured_products}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "pRODUCTS"
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()[4:]
    # products = getProduct("static/products_list.json")
    content = {"title": title, "links_menu": links_menu, "products": products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "cONTACTS"
    locations = Contact.objects.all()
    vizit_date = timezone.now()
    content = {"title": title, "locations": locations, "vizit_date": vizit_date}
    return render(request, "mainapp/contact.html", content)


def history(request):
    title = "hISTORY"
    content = {"title": title}
    return render(request, "mainapp/history.html", content)


def showroom(request, pk=None):
    title = "sHOWROOM"
    links_menu = ProductCategory.objects.all()
    content = {"title": title, "links_menu": links_menu}
    return render(request, "mainapp/showroom.html", content)

