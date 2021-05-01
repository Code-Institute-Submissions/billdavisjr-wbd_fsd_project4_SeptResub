from django.shortcuts import render, get_object_or_404
from .models import Quotation

# Create your views here.


def all_quotations(request):
    """ View to show all quotations, as well as sorting, searching  """

    quotations = Quotation.objects.all()

    context = {
        'quotations': quotations,
    }

    return render(request, 'quotations/quotations.html', context)


def quotation_detail(request, quotation_id):
    """ View to show all record detail for a particular quotation  """

    quotation = get_object_or_404(Quotation, pk=quotation_id)

    context = {
        'quotation': quotation,
    }

    return render(request, 'quotations/quotation_detail.html', context)
