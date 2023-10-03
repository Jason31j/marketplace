import django.forms as forms
from .models import Product

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

class categoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
