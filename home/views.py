from django.shortcuts import render
from django.db.models import Q
from quotations.models import Quotation, Category
from random import randint

# Create your views here.


def index(request):
    """ A view to return the index page of the home app (of the site) """

    categories = Category.objects.all()
    quotations = Quotation.objects.all()

    # Disabling searching for quotes with "quot" (quote/quotes/quotation) in it
    # since we don't have enough of them gathered for a decent random choice of
    # quotes about qoutes; instead choose a random quote from the entire
    # database for now until more can be added.
    
    # query = 'quot'
    query = ''

    # choose quote to display at random from those containing 'quot'
    # (which gets use quote, quotes, quotation, quoted, quoting, etc.)

    quote_quotes = Q(text__icontains=query)
    quotations = quotations.filter(quote_quotes)

    # Get number of quotes returned and pick one at random

    if quotations.count():
        qc = quotations.count()
        rc = randint(0, qc-1)
        # print("Chose quote #", rc, "of", qc)
        randomquote = quotations[rc]
        print(randomquote)
    else:
        randomquote = '"I love quotations because it is a joy to '
        + 'find thoughts one might have, beautifully '
        + 'expressed with much authority by someone '
        + 'recognized wiser than oneself."  -- Marlene Dietrich'

    context = {
        'quotations': quotations,
        'categories': categories,
        'search_term': query,
        'randomquote': randomquote,
    }

    return render(request, 'home/index.html', context)
