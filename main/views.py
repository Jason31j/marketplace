from django.views import generic

# Create your views here.

class home(generic.TemplateView):
    template_name = 'main/index.html'