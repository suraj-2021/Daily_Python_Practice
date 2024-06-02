from django import forms
from.models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
         model = Item
         fields=('category','name','description','image')




class EditItemForm(forms.ModelForm):
    class Meta:
         model = Item
         fields=('name','description','image','is_sold')


