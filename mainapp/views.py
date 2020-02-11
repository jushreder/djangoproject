from django.shortcuts import render
import json


def getProduct(name_file):
    json_data = open(name_file)
    product_list = json.load(json_data)
    json_data.close()
    return product_list

# Create your views here.

def main(request):
    title = 'hOME'
    featured_products = getProduct('static/products.json')
    content= {'title' : title, 'featured_products' : featured_products}
    return render(request, 'mainapp/index.html', content)
    
def products(request):
    title = 'pRODUCTS'
    links_menu = [
        {"href": "products_all", "name": "all"},
        {"href": "products_home", "name": "home"},
        {"href": "products_office", "name": "office"},
        {"href": "products_furniture", "name": "futniture"},
        {"href": "products_modern", "name": "modern"},
        {"href": "products_classic", "name": "classic"},
    ]
    products = getProduct('static/products_list.json')
    content= {'title' : title, 'links_menu': links_menu, 'products' : products}
    return render(request, 'mainapp/products.html', content)
    
def contact(request):
    title = 'cONTACTS'
    locations=[
        {
        'city' : 'CALIFORNIA',
        'phone': '1900-1234-5678',
        'email': 'info@iterior.com',
        'address': '12 W 1st St, 90001 Los Angeles, California'
        },
        {
        'city' : 'CALIFORNIA',
        'phone': '1900-5678-1234',
        'email': 'info@iterior.com',
        'address': '9 W 2st St, 90001 Los Angeles, California'
        },
        {
        'city' : 'CALIFORNIA',
        'phone': '1900-8765-4321',
        'email': 'info@iterior.com',
        'address': '10 W 3st St, 90001 Los Angeles, California'
        }, 
    ]
    content ={'title' : title, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)

def history(request):
    title = 'hISTORY'
    content ={'title' : title}
    return render(request, 'mainapp/history.html', content)

def showroom(request):
    title = 'sHOWROOM'
    links_menu = [
        {"href": "showroom_all", "name": "all"},
        {"href": "showroom_home", "name": "home"},
        {"href": "showroom_office", "name": "office"},
        {"href": "showroom_furniture", "name": "futniture"},
        {"href": "showroom_modern", "name": "modern"},
        {"href": "showroom_classic", "name": "classic"},
    ]
    content ={'title' : title, 'links_menu' : links_menu}
    return render(request, 'mainapp/showroom.html', content)

