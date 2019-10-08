from django.contrib import admin
from .models import Product,Feedback

class FeedbackAdmin(admin.ModelAdmin):
	list_display=('product','customer_name','date',)

	class Meta:
		model=Feedback

admin.site.register(Feedback,FeedbackAdmin)	
admin.site.register(Product)	
