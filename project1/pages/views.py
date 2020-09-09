from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from listings.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:2]
    context = {
        'listing_pagekey' : listings,
        'state_choices' : state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors_pages': realtors,
        'mvp_realtors' : mvp_realtors

    }

    return render(request, 'pages/about.html', context)