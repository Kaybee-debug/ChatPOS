from django import forms
from .models import Business,Product
# class BankForm(forms.ModelForm):
#     class Meta:
#         model =Bank
#         fields =[
#             "bank_name",
#             "image",
#             "interest_rate", 
#         ]


class BusinessForm(forms.ModelForm):
    
    class Meta:
        model = Business
        fields = "__all__"  
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"         