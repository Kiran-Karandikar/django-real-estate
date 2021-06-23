from django.contrib import messages
from django.shortcuts import redirect, render


# Create your views here.
def register(request):
    """

    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        messages.error(request, "This is test message for testing")
        # messages.info(request, "Testing message for info level")
        return redirect("register")
    return render(request, "accounts/register.html")


def logout(request):
    """

    Args:
        request:

    Returns:

    """
    return redirect('index')


def login(request):
    """

    Args:
        request:

    Returns:

    """
    if request.method is "POST":
        pass
    return render(request, "accounts/login.html")


def dashboard(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "accounts/dashboard.html")
