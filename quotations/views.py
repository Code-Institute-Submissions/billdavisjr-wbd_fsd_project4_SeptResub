from django.shortcuts import render
from .models import Quotation

# Create your views here.


def all_quotations(request):
    """ View to show all quotations, as well as sorting, searching  """

    quotations = Quotation.objects.all()

    context = {
        'quotations': quotations,
    }

    return render(request, 'quotations/quotations.html', context)
