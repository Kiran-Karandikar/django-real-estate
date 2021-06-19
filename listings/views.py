"""
# Docstring
"""
# todo -> pagination imports
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Listing
# Create your views here.


def base_listings(request):
    """
    Serve all listings.
    Args:
        request:

    Returns:

    """
    all_listings = Listing.objects.all()
    # todo
    # Implementing pagination

    # paginated = Paginator(all_listings, 2)
    # request_page = request.GET.get("page")
    # paginated_listings = paginated.get_page(request_page)

    context = {
            "listings": all_listings,
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
    context = {
            "single_listing": listing_id
    }
    return render(request, "listings/listing.html", context)
