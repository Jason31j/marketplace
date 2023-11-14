from django import forms

from .models import Review, StoreReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['tittle', 'rating', 'description', 'image']

    tittle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

class StoreReviewForm(forms.ModelForm):
    class Meta:
        model = StoreReview
        fields = ['tittle', 'rating', 'description', 'image']

    tittle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
