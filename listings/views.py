from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def listing_home(request):
    """

    Args:
        request:

    Returns:

    """
    # return HttpResponse("<h1>listings app up and running</h1>")
    return render(request, "listings/listing_page.html")