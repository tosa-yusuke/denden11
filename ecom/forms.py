from django import forms

class Product_form(forms.Form):
    number = forms.IntegerField(label="number")
