from django.contrib import admin

# import your models here.

from .models import Quotation, Category

# Register your models here.


class QuotationAdmin(admin.ModelAdmin):
    # columns from model to display in admin interface
    list_display = (
            'pk',
            'text',
            'person',
            'category',
            'dateSaid',
            'stars',
            'favorite', )

    # sort order and fields; to reviser put a - in front of field name
    ordering = ('person', 'text', )


class CategoryAdmin(admin.ModelAdmin):
    # columns from model to display in admin interface
    list_display = ('pk', 'display_name', 'name')

    # sort order and fields; to reviser put a - in front of field name
    ordering = ('display_name', )


admin.site.register(Quotation, QuotationAdmin)
admin.site.register(Category, CategoryAdmin)
