from django.contrib import messages
from django.shortcuts import redirect, render


# Create your views here.

def inquiry(request):
    """

    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        messages.success(request, "Made contact inquiry")
        return redirect('index')
    return render(request, "contacts/base.html")
