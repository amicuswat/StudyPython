from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

class RawProductForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={
		"placeholder": "Product title"
	}))
	description = forms.CharField(required=False,
		widget=forms.Textarea(
			attrs={
				"placeholder": "Input product description",
				"class": "new-class-name",
				"id": "my-id-for-textarea",
				"rows": 20,
				"cols": 120
			}
		)
	)
	price = forms.DecimalField(initial=19.99)
