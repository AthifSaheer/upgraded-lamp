from user_panel.models import *
from django import forms


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['title', 'slug', 'category', 'sub_category', 'image', 'marked_price']
        fields = ('__all__')
        # widgets = {
        #     'color': forms.TextInput(attrs={'type': 'color'}),
        # }

class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')

class CreateSubCategory(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('__all__')

class ChangeProfileImageForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ['image',]