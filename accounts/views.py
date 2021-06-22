from django.shortcuts import render


# Create your views here.
def register(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "accounts/register.html")


def logout(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "accounts/register.html")


def login(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "accounts/login.html")


def dashboard(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "accounts/dashboard.html")
