from django.contrib import admin

# import your models here.
from .models import Quotation, Category

# Register your models here.
admin.site.register(Quotation)
admin.site.register(Category)
