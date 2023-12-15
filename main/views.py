from django.views import generic
from products.models import Product

# Create your views here.

class home(generic.TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('-rating')[:4]
        print(context['products'])
        return context