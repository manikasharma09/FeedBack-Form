from django.db import models
from django.utils import timezone

class Product(models.Model):
	name=models.CharField(max_length=120)
	def __str__(self):
		return self.name

class Feedback(models.Model):
	customer_name=models.CharField(max_length=120)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	details=models.TextField(blank=True)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.customer_name

