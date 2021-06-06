from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    """

    Args:
        request:

    Returns:

    """
    # return HttpResponse("HI there")
    return render(request, "pages/index.html")

def about(request):
    """

    Args:
        request:

    Returns:


    """
    return render(request, "pages/about.html")
    # return HttpResponse("This works!!!")
