from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect

# Create your views here.
from django.conf import settings
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from adminapp.forms import ProductCategoryEditForm, ShopUserAdminEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from mainapp.models import Product, ProductCategory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = "adminapp/users.html"

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context["title"] = "админка/пользователи"
        return context 

class UserCreateView(LoginRequiredMixin, CreateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy("admin:users")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["title"] = "пользователи/создание"
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy("admin:users")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context["title"] = "пользователи/редактирование"
        return context 

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = ShopUser
    template_name = "adminapp/user_delete.html"
    success_url = reverse_lazy("admin:users")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context["title"] = "пользователи/удаление"
        return context

class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = "adminapp/categories.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context["title"] = "админка/категории"
        return context

class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context["title"] = "категории/создание"
        return context

class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context["title"] = "категории/редактирование"
        return context 

class ProductCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy("admin:categories")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        context["title"] = "категории/удаление"
        return context

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/products.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = "продукт/создание"
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse("admin:products", args=[pk]))
    else:
        product_form = ProductEditForm(initial={"category": category})

    content = {"title": title, "update_form": product_form, "category": category, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/product_update.html", content)

class ProductDetailView(LoginRequiredMixin,  DetailView):
    model = Product
    template_name = "adminapp/product_read.html"
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["title"] = "продукт/подробнее"
        return context
   
@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = "продукт/редактирование"
    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("admin:product_update", args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {
        "title": title,
        "update_form": edit_form,
        "category": edit_product.category,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "adminapp/product_update.html", content)

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = "продукт/удаление"
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse("admin:products", args=[product.category.pk]))

    content = {"title": title, "product_to_delete": product, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/product_delete.html", content)