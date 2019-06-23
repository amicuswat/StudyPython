from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		#form.ProductForm()

	context = {
		'form':form
	}
	return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
	obj = Product.objects.get(id=id)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
		'object':obj
	}
	return render(request, "products/product_detail.html", context)

def product_update_view(request, id):
	initial_data = {
		'title': "This is my awaresome title"
	}
	obj = Product.objects.get(id=id)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	print(request.method)
	if request.method == "POST":
		#confirming delete
		obj.delete()
		print("I tried to delete the product")
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "products/product_delete.html", context)

# def dynamic_lookup_view(request, id):
	#obj = Product.objects.get(id=id)
	obj = get_object_or_404(Product, id=id)
	# try:
	# 	obj = Product.objects.get(id=id)
	# except Product.DoesNotExist:
	# 	raise Http404
	context = {
		"object": obj
	}
	return render(request, "products/product_detail.html", context)

# def product_create_view1(request):
# 	#print(request.GET)
# 	#print(request.POST)
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 		# Product.objects.create(title=my_new_title)
# 	context = {}
# 	return render(request, "products/product_create.html", context)
