from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Quotation, Category
from .forms import QuotationForm, CategoryForm

# Create your views here.


def all_quotations(request):
    """ View to show all quotations, as well as sorting, searching  """

    quotations = Quotation.objects.all()
    categories = Category.objects.all()

    total_quotations = quotations.count()

    query = None
    category_list = None
    sort = None
    direction = None

    if request.GET:
        #
        # TODO - allow multiple categories at once and filter through code below to get final result.
        # TODO - reorder these; sort last
        # 
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

        # TODO - should the following to (person, q) be FIRST? 

        if 'person' in request.GET:
            query = request.GET['person']
            queries = Q(person__icontains=query)
            quotations = quotations.filter(queries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't provide anything to search for!")
                return redirect(reverse('quotations'))

            queries = Q(text__icontains=query) | Q(person__icontains=query)
            quotations = quotations.filter(queries)

    current_sorting = f'{sort}_{direction}'
    # Note: above variable will be None_None if no sorting

    count = quotations.count()

    if count == 0:
        if query != None:
            messages.error(request, f'No results found for your search words: "{query}" ')

        return redirect(reverse('quotations'))

    if count != total_quotations:
        if query != None:
            messages.info(request, f'{count} quotes found of {total_quotations} in database containing "{query}"')
        else: 
            messages.info(request, f'{count} quotes found of {total_quotations} in database')
    else:
        messages.info(request, f'{total_quotations} quotes in database')

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

    try:
        quotation = get_object_or_404(Quotation, pk=quotation_id)
    except Exception as e:
        messages.error(request, f'ERROR: {e}')
        return redirect(reverse('quotations'))

    context = {
        'quotation': quotation,
    }

    return render(request, 'quotations/quotation_detail.html', context)


# login and super-user required disabled until we support accounts fully
# @login_required
def add_quotation(request):
    """ Add a quotation to the database """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only site owners can do that.')
    #     return redirect(reverse('home'))

    if request.method == 'POST':
        form = QuotationForm(request.POST, request.FILES)
        if form.is_valid():
            quotation = form.save()
            messages.success(request, 'Successfully added quotation!')
            return redirect(reverse('quotation_detail', args=[quotation.id]))
            # return redirect(reverse('add_quotation'))
        else:
            messages.error(request,
                           ('Failed to add quotation. '
                            'Please ensure the information on the form is valid.'))
    else:
        form = QuotationForm()

    template = 'quotations/add_quotation.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

# login and super-user required disabled until we support accounts fully
#@login_required
def edit_quotation(request, quotation_id):
    """ Edit a quotation in the database """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only site owners can do that.')
    #     return redirect(reverse('home'))

    quotation = get_object_or_404(Quotation, pk=quotation_id)

    if request.method == 'POST':
        form = QuotationForm(request.POST, request.FILES, instance=quotation)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated quotation #{ quotation.id }!')
            return redirect(reverse('quotation_detail', args=[quotation.id]))
        else:
            messages.error(request,
                           ('Failed to update quotation. '
                            'Please ensure the form is valid.'))
    else:
        form = QuotationForm(instance=quotation)
        messages.info(request, f'You are editing quotation #{quotation.id}')

    template = 'quotations/edit_quotation.html'
    context = {
        'form': form,
        'quotation': quotation,
    }

    return render(request, template, context)


#@login_required
def delete_quotation(request, quotation_id):
    """ Delete a quotation from the database """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only site owners can do that.')
    #     return redirect(reverse('home'))

    try:
        quotation = get_object_or_404(Quotation, pk=quotation_id)
        quotation.delete()
        messages.success(request, f'Quotation #{quotation_id} deleted!')
        return redirect(reverse('quotations'))
    except Exception as errmsg:
        messages.error(request, f'Unable to delete quotation #{quotation_id}; error:  {errmsg}')
        return redirect(reverse('quotation_detail', args=[quotation.id]))

    return redirect(reverse('quotations'))


def all_categories(request):
    """ View to show all categories """

    categories = Category.objects.all()
    total_categories = categories.count()

    sortkey = 'lower_name'
    categories = categories.annotate(lower_name=Lower('name'))
    categories = categories.order_by(sortkey)

    messages.info(request, f'{total_categories} categories')

    context = {
        'categories': categories,
    }

    return render(request, 'quotations/categories.html', context)


# login and super-user required disabled until we support accounts fully
# @login_required
def add_category(request):
    """ Add a quotation to the database """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only site owners can do that.')
    #     return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Successfully added category #{category.id}: {category.display_name}')
            return redirect(reverse('categories'))
        else:
            messages.error(request,
                           ('Failed to add category.'
                            'Please ensure the information on the form is valid.'))
    else:
        form = CategoryForm()

    template = 'quotations/add_category.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


# login and super-user required disabled until we support accounts fully
# @login_required
def edit_category(request, category_id):
    """ Edit a category in the database """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only site owners can do that.')
    #     return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Updated category #{ category.id }: { category.display_name }')
            return redirect(reverse('categories'))
        else:
            messages.error(request,
                           ('Failed to update category. '
                            'Please ensure the form is valid.'))
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing category #{category.id}: {category.display_name}')

    template = 'quotations/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


#@login_required


# @login_required
def delete_category(request, category_id):
    """ Delete a category from the database """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only site owners can do that.')
    #     return redirect(reverse('home'))

    try:
        category = get_object_or_404(Category, pk=category_id)
        category.delete()
        messages.success(request, f'Category #{category_id}: "{category.name}" deleted!')
        return redirect(reverse('categories'))
    except Exception as errmsg:
        messages.error(request, f'Unable to delete category #{category_id}: "{category.name}"; error:  {errmsg}')
        return redirect(reverse('categories'))

    return redirect(reverse('categories'))

