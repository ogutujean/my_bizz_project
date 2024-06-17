from django import forms

class CartAddProductForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(
        min_value=1,
        max_value=100,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        # Add any custom validation for quantity here
        return data
