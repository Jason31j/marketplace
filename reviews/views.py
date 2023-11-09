from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.urls import reverse
from django.views import generic

from .models import Review
from .forms import ReviewForm

# Create your views here.

class ReviewListView(generic.ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        return Review.objects.filter(product=self.kwargs['id_product'])


class ReviewCreateView(LoginRequiredMixin ,generic.CreateView):
    model = Review
    template_name = 'review_create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        try:
            form.instance.product_id = self.kwargs['id_product']
            form.instance.author_id = self.request.user.id
            return super().form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'You have already reviewed this product')
            return super().form_invalid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('reviews:review_list', kwargs={'id_product': self.kwargs['id_product']})


class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'review_detail.html'
    context_object_name = 'review'


class ReviewUpdateView(generic.UpdateView):
    model = Review
    template_name = 'review_update.html'
    form_class = ReviewForm
    context_object_name = 'review'

    def get_object(self):
        return Review.objects.get(id=self.kwargs['id_review'])

    def get_success_url(self):
        return reverse('reviews:review_list', kwargs={'id_product': self.object.product.id})


class ReviewDeleteView(generic.DeleteView):
    model = Review
    template_name = 'review_delete.html'
    context_object_name = 'review'

    def get_object(self):
        return Review.objects.get(id=self.kwargs['id_review'])

    def get_success_url(self):
        return reverse('reviews:review_list', kwargs={'id_product': self.object.product.id} )