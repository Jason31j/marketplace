from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .forms import categoryForm, productForm
from .models import Product, Category, Wishlist


# --------------------product views------------------------

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
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.kwargs.get('category'):
            return Product.objects.filter(category__slug=self.kwargs.get('category'))
        else:
            return Product.objects.all()


class productDetailPage(generic.DetailView):
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()


class productCreatePage(generic.CreateView):
    template_name = 'product/product_create.html'
    model = Product
    form_class = productForm

    def form_valid(self, form):
        messages.success(self.request, 'Product created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Product creation failed.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('products:product_list', kwargs={'category': self.object.category.slug})


class productUpdatePage(generic.UpdateView):
    template_name = 'product/product_update.html'
    model = Product
    form_class = productForm

    def get_success_url(self):
        return reverse('products:product_list', kwargs={'category': self.object.category.slug})

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Product update failed.')
        return super().form_invalid(form)


class productDeletePage(generic.DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    context_object_name = 'product'

    def form_valid(self, form):
        messages.success(self.request, 'Product deleted successfully.')
        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product deleted successfully.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('products:product_list', kwargs={'category': self.object.category.slug})


# --------------------category views----------------------

class categoryListPage(generic.ListView):
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# not used by now
class categoryDetailPage(generic.DetailView):
    template_name = 'category/category_detail.html'
    context_object_name = 'category'
    queryset = Category.objects.all()


class categoryCreatePage(generic.CreateView):
    template_name = 'category/category_create.html'
    model = Category
    form_class = categoryForm

    def form_valid(self, form):
        messages.success(self.request, 'Category created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Category creation failed.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('products:category_list')


class categoryUpdatePage(generic.UpdateView):
    template_name = 'category/category_update.html'
    model = Category
    form_class = categoryForm

    def form_valid(self, form):
        messages.success(self.request, 'Category updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Category update failed.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('products:category_list')


class categoryDeletePage(generic.DeleteView):
    template_name = 'category/category_delete.html'
    model = Category
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('products:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Category deleted successfully.')
        return super().delete(request, *args, **kwargs)


# -------------------- wishlist views ------------------------

class wishlistListPage(LoginRequiredMixin, generic.ListView):
    template_name = 'wishlist/wishlist_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.request.user.wishlist_set.all()


class wishlistAddPage(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('products:product_detail', kwargs={'slug': self.kwargs.get('slug'), 'category': self.kwargs.get('category')})

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(slug=self.kwargs.get('slug'))
        wishlist = self.request.user.wishlist_set.all()

        # validate if product is already in wishlist
        if wishlist.filter(product=product).exists():
            messages.error(request, 'Product already in wishlist.')
        else:
            wishlist_item = {'product': product, 'user': self.request.user}
            Wishlist.objects.create(**wishlist_item)
            messages.success(request, 'Product added to wishlist.')
        return super().get(request, *args, **kwargs)


class wishlistRemovePage(generic.DeleteView):
    template_name = 'wishlist/wishlist_delete.html'
    model = Wishlist
    context_object_name = 'product'

    def get_object(self):
        return Wishlist.objects.get(id=self.kwargs['wishlist_item'])

    def get_success_url(self):
        return reverse('products:wishlist_list')

    def form_valid(self, form):
        messages.success(self.request, 'Product removed from wishlist.')
        return super().form_valid(form)