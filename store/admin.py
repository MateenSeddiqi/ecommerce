from django.contrib import admin
from .models import Store, CustomUser,Category,Product
# Register your models here.
admin.site.register(Store)
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Product)