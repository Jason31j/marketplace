from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Product, Category
from .forms import categoryForm, productForm


#product views

#coming soon
def productSearchPage(request):
    template_name = 'product_search.html'
    context_object_name = 'products'
    if request.method == 'POST':
        search = request.POST.get('search')
        products = Product.objects.filter(name__contains=search)
        return render(request, template_name, {context_object_name: products})
    else:
        return redirect('/products/')
class productListPage(generic.ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.kwargs.get('category'):
            return Product.objects.filter(category__slug=self.kwargs.get('category'))
        else:
            return Product.objects.all()


class productDetailPage(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

class productCreatePage(generic.CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = productForm

    def get_success_url(self):
        return reverse('products:product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Product created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Product creation failed.')
        return super().form_invalid(form)

class productUpdatePage(generic.UpdateView):
    template_name = 'product_update.html'
    model = Product
    fields = ['name', 'price', 'description', 'image']

    def get_success_url(self):
        return reverse('products:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Product update failed.')
        return super().form_invalid(form)

class productDeletePage(generic.DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('products:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Product deleted successfully.')
        return super().form_valid(form)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product deleted successfully.')
        return super().delete(request, *args, **kwargs)

#category views
class categoryListPage(generic.ListView):
    template_name = 'category_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

class categoryDetailPage(generic.DetailView):
    template_name = 'category_detail.html'
    context_object_name = 'category'
    queryset = Category.objects.all()

class categoryCreatePage(generic.CreateView):
    template_name = 'category_create.html'
    model = Category
    form_class = categoryForm

    def get_success_url(self):
        return reverse('products:category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Category created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Category creation failed.')
        return super().form_invalid(form)

class categoryUpdatePage(generic.UpdateView):
    template_name = 'category_update.html'
    model = Category
    form_class = categoryForm

    def get_success_url(self):
        return reverse('products:category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Category updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Category update failed.')
        return super().form_invalid(form)

class categoryDeletePage(generic.DeleteView):
    template_name = 'category_delete.html'
    model = Category
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('products:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Category deleted successfully.')
        return super().delete(request, *args, **kwargs)
