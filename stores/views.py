# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views import generic
from .models import Store

class storeListPage(generic.ListView):
    template_name = 'store_list.html'
    context_object_name = 'stores'
    queryset = Store.objects.all()
    
class storeDetailPage(generic.DetailView):
    template_name = 'store_detail.html'
    context_object_name = 'store'
    queryset = Store.objects.all()

class storeCreatePage(generic.CreateView):
    template_name = 'store_create.html'
    model = Store
    fields = ['name', 'address', 'phone', 'email', 'description', 'image']
    success_url = '/store/'

    def form_valid(self, form):
        messages.success(self.request, 'Store created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Store creation failed.')
        return super().form_invalid(form)

class storeUpdatePage(generic.UpdateView):
    template_name = 'store_update.html'
    model = Store
    fields = ['name', 'address', 'phone', 'email', 'description', 'image']

    def form_valid(self, form):
        messages.success(self.request, 'Store updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Store update failed.')
        return super().form_invalid(form)

class storeSearchPage(generic.ListView):
    template_name = 'store_search.html'
    context_object_name = 'store'
    queryset = Store.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Store.objects.filter(name__contains=query)

class storeDeletePage(generic.DeleteView):
    template_name = 'store_delete.html'
    model = Store
    success_url = '/store/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Store deleted successfully.')
        return super().delete(request, *args, **kwargs)