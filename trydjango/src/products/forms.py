from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={
		"placeholder": "Product title"
	}))
	#email = forms.EmailField()
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
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]
	# def clean_title(self, *args, **kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if not "CFE" in title:
	# 		raise forms.ValidationError("This is not a valid title - add CFE")
	# 	if not "news" in title:
	# 		raise forms.ValidationError("This is not a valid title - add news")
	# 	return title
	#
	# def clean_email(self, *args, **kwargs):
	# 	email = self.cleaned_data.get("email")
	# 	if not email.endswith("edu"):
	# 		raise forms.ValidationError("This is not a valid email")
	# 	return email

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
