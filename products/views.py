from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.contrib import messages
from .models import Product
from .forms import categoryForm, productForm


# Create your views here.
class productListPage(generic.ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

class productDetailPage(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

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
class productCreatePage(generic.CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = productForm
    success_url = '/products/'

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

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Product update failed.')
        return super().form_invalid(form)

class productDeletePage(generic.DeleteView):
    template_name = 'product_delete.html'
    model = Product
    success_url = '/products/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product deleted successfully.')
        return super().delete(request, *args, **kwargs)
