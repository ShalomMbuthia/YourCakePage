from django import forms
from mycake.models import CakesAndEquipments#ImageModel

class CakesAndEquipments(forms.ModelForm):
    class Meta:
        model = CakesAndEquipments
        fields = ['name','price','description','origin','color']

#class ImageUploadForm(forms.ModelForm):
   # class Meta:
       # model = ImageModel
        #fields = ['image','title','price']
