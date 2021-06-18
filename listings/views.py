from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
# Create your views here.


def base_listings(request):
    """

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