from django import forms
from store.models import Experts, Products, Recipes, Videos
 
 
class ExpertForm(forms.ModelForm):
 
    class Meta:
        model = Experts
        fields = ['name', 'image', 'user_id']


class ProductForm(forms.ModelForm):
 
    class Meta:
        model = Products
        fields = ['title', 'image', 'price', 'category']


class RecipesForm(forms.ModelForm):
 
    class Meta:
        model = Recipes
        fields = ['title', 'image', 'description']

class VideotForm(forms.ModelForm):
 
    class Meta:
        model = Videos
        fields = ['title', 'image', 'note', 'video', 'section', 'expert_id']

