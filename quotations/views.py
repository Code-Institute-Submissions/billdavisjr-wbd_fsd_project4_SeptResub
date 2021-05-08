from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Quotation, Category
from django.db.models.functions import Lower

# Create your views here.


def all_quotations(request):
    """ View to show all quotations, as well as sorting, searching  """

    quotations = Quotation.objects.all()
    categories = Category.objects.all()

    query = None
    category_list = None
    sort = None
    direction = None
    person = None

    if request.GET:
        # sort by person, stars, category
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'person':
                sortkey = 'lower_person'
                quotations = quotations.annotate(lower_person=Lower('person'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            quotations = quotations.order_by(sortkey)

        if 'category' in request.GET:
            # Note: following supports more than one category, separated
            # by commans, for future use:
            category_filter = request.GET['category'].split(',')
            # to display category(s) filtered if we want:
            category_list = Category.objects.filter(name__in=category_filter)
            quotations = quotations.filter(category__name__in=category_filter)

        if 'person' in request.GET:
            query = request.GET['person']
            print(query)
            queries = Q(person__icontains=query)
            print(queries)
            quotations = quotations.filter(queries)
            print(quotations)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't provide anything to search for!")
                return redirect(reverse('quotations'))

            queries = Q(text__icontains=query) | Q(person__icontains=query)
            quotations = quotations.filter(queries)

    current_sorting = f'{sort}_{direction}'
    # Note: above variable will be None_None if no sorting

    context = {
        'quotations': quotations,
        'categories': categories,
        'category_list': category_list,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'quotations/quotations.html', context)


def quotation_detail(request, quotation_id):
    """ View to show all record detail for a particular quotation  """

    quotation = get_object_or_404(Quotation, pk=quotation_id)

    context = {
        'quotation': quotation,
    }

    return render(request, 'quotations/quotation_detail.html', context)
