from django.shortcuts import get_object_or_404,render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published= True)
    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings_key': paged_listings
    }
    return render(request, 'listing/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    internal_photos = []
    for i in range(1, 7):
        if getattr(listing, 'photo_%d' % i):
            photo = getattr(listing, 'photo_%d' % i)
            internal_photos.append(photo)
    context = {
        'listings_404': listing,
        'internal_photos': internal_photos
    }
    return render(request, 'listing/listing.html',context)

def search(request):
    queryset_list= Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact= city)


    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__icontains=state)


    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)



    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings_queryset': queryset_list,
        'values': request.GET
    }

    return render(request, 'listing/search.html',context)