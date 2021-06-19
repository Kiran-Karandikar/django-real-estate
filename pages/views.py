from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing


def index(request):
    """

    Args:
        request:

    Returns:

    """
    top_listings = \
        Listing.objects.order_by('-list_date').filter(is_published= True)[:3]
    context = {
            "top_listings": top_listings
    }
    return render(request, "pages/index.html", context)


def about(request):
    """

    Args:
        request:

    Returns:


    """
    all_realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp = True)
    context = {
            "realtors": all_realtors,
            "mvp_realtors": mvp_realtors
    }
    return render(request, "pages/about.html", context)
