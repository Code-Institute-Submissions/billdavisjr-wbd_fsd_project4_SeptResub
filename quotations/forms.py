from django import forms
from .models import Quotation, Category

class QuotationForm(forms.ModelForm):

    class Meta:
            model = Quotation
            fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            field.widget.attrs['id'] = field_name


class CategoryForm(forms.ModelForm):

    class Meta:
            model = Category
            fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            field.widget.attrs['id'] = field_name
