from django import forms
from .models import Product

class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

'''
#I was unable to get validation errors to show up on the front end
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if (title == ""):
            print('incorrect')
            raise forms.ValidationError('This field cannot be left blank')
        return title'''