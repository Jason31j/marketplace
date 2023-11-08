# Create your views here.
from django.contrib import messages
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Store
from .forms import StoreForm
class storeListPage(generic.ListView):
    template_name = 'store/store_list.html'
    context_object_name = 'stores'
    queryset = Store.objects.all()

class storeDetailPage(generic.DetailView):
    template_name = 'store/store_detail.html'
    context_object_name = 'store'
    queryset = Store.objects.all()

class storeCreatePage(LoginRequiredMixin, generic.CreateView):
    template_name = 'store/store_create.html'
    model = Store
    form_class = StoreForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        messages.success(self.request, 'Store created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Store creation failed.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('stores:store_list')

class storeUpdatePage(generic.UpdateView):
    template_name = 'store/store_update.html'
    model = Store
    form_class = StoreForm

    def form_valid(self, form):
        messages.success(self.request, 'Store updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Store update failed.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('stores:store_list')

class storeDeletePage(generic.DeleteView):
    template_name = 'store/store_delete.html'
    model = Store
    content_object_name = 'store'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Store deleted successfully.')
        return super().delete(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('stores:store_list')

class myStorePage(LoginRequiredMixin ,generic.TemplateView):
    template_name = 'store/my_store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega objetos filtrados al contexto
        context['store'] = Store.objects.filter(user=self.request.user)
        return context

#comming soon
class storeSearchPage(generic.ListView):
    template_name = 'store_search.html'
    context_object_name = 'store'
    queryset = Store.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Store.objects.filter(name__contains=query)