from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello world</h1>")
	return render(request, "home.html", {})

def contacts_view(request, *args, **kwargs):
	return render(request, "contacts.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"title": "this page is about me",
		"my_number": 123,
		"my_list": [123, 321, 4242, 12313, "abc"],
		"my_html": "<h1> Hello world </h1>"
	}
	return render(request, "about.html", my_context)

def social_view(*args, **kwargs):
	return HttpResponse("<h1>Social page</h1>")