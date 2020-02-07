from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')
    
def products(request):
    return render(request, 'mainapp/products.html')
    
def contact(request):
    return render(request, 'mainapp/contact.html')

def history(request):
    return render(request, 'mainapp/history.html')

def showroom(request):
    return render(request, 'mainapp/showroom.html')

