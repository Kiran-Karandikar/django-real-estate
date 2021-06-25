from django.shortcuts import render


# Create your views here.

def inquiry(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "contacts/base.html")
