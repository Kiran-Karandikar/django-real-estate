"""
# Docstring
"""
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from btre.constants import *
from .models import Listing


# Create your views here.


def base_listings(request):
    """
    Serve all listings.
    Args:
        request:

    Returns:

    """
    all_listings = Listing.objects.order_by('-list_date').filter(
        is_published = True)
    paginated = Paginator(all_listings, 2)
    requested_page = request.GET.get("page")
    paginated_listings = paginated.get_page(requested_page)

    context = {
            # "listings": all_listings,
            "listings": paginated_listings,
            # "listings_temp": paginated_listings,
    }
    return render(request, "listings/listings.html", context)


def individual_listing(request, listing_id):
    """
    For individual listing
    Args:
        request:
        listing_id:

    Returns:

    """
    single_listing = get_object_or_404(Listing, pk = listing_id)
    context = {
            "single_listing": single_listing
    }
    return render(request, "listings/listing.html", context)


def search(request, **kwargs):
    """

    Args:
        request:
    """
    search_result_set = Listing.objects.order_by("-list_date").filter(
        is_published = True)
    context = {
            "us_states": us_states, "bedrooms": bedrooms,
            "max_price": max_price,
    }
    if 'keywords' in request.GET:
        keywords = request.GET["keywords"]
        if keywords and search_result_set:
            search_result_set = search_result_set.filter(
                description__icontains = keywords)
    if 'city' in request.GET:
        city = request.GET["city"]
        if city and search_result_set:
            search_result_set = search_result_set.filter(
                city__iexact = city.strip())
    if 'state' in request.GET:
        state = request.GET["state"]
        if state and search_result_set:
            search_result_set = search_result_set.filter(
                state__iexact = state.strip())
    if 'bedrooms' in request.GET:
        bedroom = int(request.GET["bedrooms"])
        if bedroom and search_result_set:
            search_result_set = search_result_set.filter(
                bedrooms__lte = bedroom)
    if 'price' in request.GET:
        price = int(request.GET["price"])
        if price and search_result_set:
            search_result_set = search_result_set.filter(price__lte = price)

    context["search_result"] = search_result_set
    context["GetRequestValue"] = request.GET

    # feature
    # how to implement cookies to store the values of search fields across
    # multiple requests -->
    # This is for first page, since on first page the get request will have
    # search fields but not `page` and on subsequents paginated pages the get
    # request will not have any of search fields resulting in clearing of
    # the search form.

    # if "page" not in request.GET:
    #     context["GetRequestValue"] = request.GET

    # feature
    # this is test pagination

    # paginated_search_result = Paginator(search_result_set, 2)
    # requested_page = 1
    # if "page" in request.GET:
    #     requested_page = request.GET["page"]
    # search_result_set = paginated_search_result.get_page(requested_page)

    # bug
    # since in template `search_result_set` is iterated, need to find a way
    # to make it iterable in case it is single item

    # if len(search_result_set) == 1:
    #     search_result_set = list(search_result_set)

    return render(request, "listings/search.html", context)
