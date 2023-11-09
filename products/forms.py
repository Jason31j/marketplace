from django import forms

from .models import Product, Category

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 1}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 0.01}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    
class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
