from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from contacts.models import Contacts


# Create your views here.
def register(request):
    """

    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        # messages.error(request, "This is test message for testing")
        # # messages.info(request, "Testing message for info level")
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, "User name is already taken !!")
                return redirect("register")
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,
                        "User with this email id already exists")
                    return redirect("register")
                else:
                    new_user = User.objects.create_user(username = username,
                        email = email, first_name = first_name,
                        last_name = last_name, password = password)

                    # new_user.save()
                    # messages.success(request, "Successfully created user")
                    # return redirect("login")

                    # feature
                    # Automatically login user after registration
                    auth.login(request, new_user)
                    messages.success(request, "Successfully created user")
                    return redirect("index")

        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")
        return redirect("register")
    return render(request, "accounts/register.html")


def logout(request):
    """

    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are successfully logged out...")
        return redirect('index')


def login(request):
    """

    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # First authenticate user
        authenticated_user = auth.authenticate(username = username,
            password = password)
        if authenticated_user is not None:
            auth.login(request, authenticated_user)
            messages.success(request, "Logged In successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Credentials !!!")
            return redirect("login")

    return render(request, "accounts/login.html")


def dashboard(request):
    """

    Args:
        request:

    Returns:

    """
    get_user_inquiries = Contacts.objects.filter(
        user_id = int(request.user.id)).order_by("-contact_date")

    context = {
            "user_inquiries": get_user_inquiries
    }
    return render(request, "accounts/dashboard.html", context)
