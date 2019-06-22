"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from pages.views import contacts_view
from pages.views import about_view
from pages.views import social_view
from products.views import (
    # product_detail_view,
    # product_create_view,
    # render_initial_data,
    dynamic_lookup_view
    )

urlpatterns = [
    path('products/<int:id>/', dynamic_lookup_view, name='product'),
    # path('', home_view, name='home'),
    # path('contacts/', contacts_view, name='contacts'),
    # path('about/', about_view, name='about'),
    # path('create/', render_initial_data, name='create'),
    # path('product/', product_detail_view, name='product'),
    # path('admin/', admin.site.urls),
]
