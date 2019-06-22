from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def render_initial_data(request):
	initial_data = {
		'title': "This is my awaresome title"
	}
	obj = Product.objects.get(id=1)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

# def product_create_view(request):
# 	#print(request.GET)
# 	#print(request.POST)
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 		# Product.objects.create(title=my_new_title)
# 	context = {}
# 	return render(request, "products/product_create.html", context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form.ProductForm()

	context = {
		'form':form
	}
	return render(request, "products/product_create.html", context)

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
		'object':obj
	}
	return render(request, "products/product_detail.html", context)
