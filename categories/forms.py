from django import forms
from . import models

class CategoryCreate(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']
'''
    def clean_name(self): # Validates the Computer Name Field
        name = self.cleaned_data.get('name')
        if (name == ""):
            raise forms.ValidationError('This field cannot be left blank')

        for instance in Category.objects.all():
            if instance.name == name:
                print('incorrect')
                message = ("Cannot have duplicate entries")
                raise forms.ValidationError(message)
        return name
'''