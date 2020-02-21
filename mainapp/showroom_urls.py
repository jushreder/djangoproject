from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [

   path('', mainapp.showroom, name='index'),
   path('category/<int:pk>/', mainapp.showroom, name='category'),
   
]