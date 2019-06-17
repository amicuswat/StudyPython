from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.TextField(default="Product name")
	description = models.TextField(default="Product description")
	price = models.TextField(default="0")
	summary = models.TextField(default="This is cool!")