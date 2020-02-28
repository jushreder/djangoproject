from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User
from authapp.models import ShopUser
import json, os


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Создаем суперпользователя при помощи менеджера модели

        super_user = ShopUser.objects.create_superuser('admin', 'django@geekshop.local', 'admin', age=33)