"""
# Docstring
"""
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

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
