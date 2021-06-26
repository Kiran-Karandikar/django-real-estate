from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Contacts


# Create your views here.

def inquiry(request):
    """

    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        user_id = request.POST["user_id"]
        listing_id = request.POST["listing_id"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        # feature
        # Use the realtor email to send mail to specific realtor using
        # django.send_email
        realtor_email = request.POST["realtor_email"]
        listing_title = request.POST["listing_title"]

        # Prevent logged in user from making multiple request per single
        # listing
        if request.user.is_authenticated:
            has_contacted = Contacts.objects.filter(
                user_id = request.user.id).exists()
            if has_contacted:
                messages.error(request, "You have already made inquiry for "
                                        "this listing")
                return redirect("/listing/" + listing_id)
        listing_inquiry = Contacts.objects.create(user_id = user_id,
            name = name, email = email, phone = phone, message = message,
            listing = listing_title, listing_id = listing_id

        )
        listing_inquiry.save()
        messages.success(request,
            "Made contact inquiry for {}".format(listing_title))
        return redirect("/listing/" + listing_id)
    return render(request, "contacts/base.html")
