from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.urls import reverse
from django.views import generic

from .models import Review, StoreReview
from .forms import ReviewForm, StoreReviewForm

# Create your views here.

class ReviewProductListView(generic.ListView):
    model = Review
    template_name = 'products/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(product=self.kwargs['id_product'])


class ReviewProductCreateView(LoginRequiredMixin ,generic.CreateView):
    model = Review
    template_name = 'products/review_create.html'
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
        return reverse('reviews:review_product_list', kwargs={'id_product': self.kwargs['id_product']})


class ReviewProductDetailView(generic.DetailView):
    model = Review
    template_name = 'products/review_detail.html'
    context_object_name = 'review'


class ReviewProductUpdateView(generic.UpdateView):
    model = Review
    template_name = 'products/review_update.html'
    form_class = ReviewForm
    context_object_name = 'review'

    def get_object(self):
        return Review.objects.get(id=self.kwargs['id_review'])

    def get_success_url(self):
        return reverse('reviews:review_product_list', kwargs={'id_product': self.object.product.id})


class ReviewProductDeleteView(generic.DeleteView):
    model = Review
    template_name = 'products/review_delete.html'
    context_object_name = 'review'

    def get_object(self):
        return Review.objects.get(id=self.kwargs['id_review'])

    def get_success_url(self):
        return reverse('reviews:review_product_list', kwargs={'id_product': self.object.product.id} )    


######################## Stores Reviews ############################

class ReviewStoreListView(generic.ListView):
    model = StoreReview
    template_name = 'stores/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return StoreReview.objects.filter(store=self.kwargs['id_store'])    


class ReviewStoreCreateView(LoginRequiredMixin ,generic.CreateView):
    model = StoreReview
    template_name = 'stores/review_create.html'
    form_class = StoreReviewForm

    def form_valid(self, form):
        try:
            form.instance.store_id = self.kwargs['id_store']
            form.instance.author_id = self.request.user.id
            return super().form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'You have already reviewed this store')
            return super().form_invalid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('reviews:review_store_list', kwargs={'id_store': self.kwargs['id_store']})


class ReviewStoreDetailView(generic.DetailView):
    model = StoreReview
    template_name = 'stores/review_detail.html'
    context_object_name = 'review'


class ReviewStoreUpdateView(generic.UpdateView):
    model = StoreReview
    template_name = 'stores/review_update.html'
    form_class = StoreReviewForm
    context_object_name = 'review'

    def get_object(self):
        return StoreReview.objects.get(id=self.kwargs['id_review'])

    def get_success_url(self):
        return reverse('reviews:review_store_list', kwargs={'id_store': self.object.store.id})


class ReviewStoreDeleteView(generic.DeleteView):
    model = StoreReview
    template_name = 'stores/review_delete.html'
    context_object_name = 'review'

    def get_object(self):
        return StoreReview.objects.get(id=self.kwargs['id_review'])

    def get_success_url(self):
        return reverse('reviews:review_store_list', kwargs={'id_store': self.object.store.id} )