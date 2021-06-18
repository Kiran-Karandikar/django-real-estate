from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
# Create your views here.


def base_listings(request):
    """
    Serve all listings.
    Args:
        request:

    Returns:

    """
    # return HttpResponse("<h1>listings app up and running</h1>")
    all_listings = Listing.objects.all()
    context = {
            "listings": all_listings
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