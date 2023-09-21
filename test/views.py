from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from django.views.generic.edit import FormView
from .models import Reservation, Room, RoomAvailability, UnavailableDate
from .forms import ReservationForm
import random
from django.http import JsonResponse
from Reservation.models import Discount
from datetime import datetime


# Create your views here.
class ReservationCreateView(FormView):
    template_name = "sample3.html"
    form_class = ReservationForm
    print("in")

    def form_valid(self, form):
        print("valid form")
        # Retrieve form data
        check_in_date = form.cleaned_data["check_in_date"]
        check_out_date = form.cleaned_data["check_out_date"]
        check_in_time = form.cleaned_data["check_in_time"]
        check_out_time = form.cleaned_data["check_out_time"]
        room_type = form.cleaned_data["room_type"]
        num_rooms = form.cleaned_data["num_rooms"]
        discount_code = form.cleaned_data[
            "discount_code"
        ]  # Get the discount_code value

        print(check_in_time)
        if discount_code:
            try:
                discount = Discount.objects.get(discountCode=discount_code, discountActive=True)
            except Discount.DoesNotExist:
                # Handle the case where the discount code is not valid or not active
                discount =  None
                return None
        else:
            discount = None  # No discount code provided, set discount to None

        # Find available rooms of the selected room type
        available_rooms = Room.objects.filter(room_type=room_type)

        # Filter available rooms by checking reservations
        reserved_rooms = Reservation.objects.filter(
            room__in=available_rooms,
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date,
        ).values_list("room", flat=True)

        # Exclude reserved rooms from available rooms
        available_rooms = available_rooms.exclude(id__in=reserved_rooms)

        if available_rooms.count() >= num_rooms:
            # Randomly select available rooms up to the requested number
            selected_rooms = random.sample(list(available_rooms), num_rooms)

            # Create a single reservation for the selected rooms
            reservation = Reservation.objects.create(
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                guest_name=form.cleaned_data["guest_name"],
                guest_email=form.cleaned_data["guest_email"],
                guest_phone=form.cleaned_data["guest_phone"],
                num_guests=form.cleaned_data["num_guests"],
                reservation_time = form.cleaned_data['reservation_time'],
                check_in_time = check_in_time,
                check_out_time =check_out_time,
            )
            # Set the selected rooms for the reservation
            reservation.room.set(selected_rooms)

            # Associate the discount code with the reservation
            if discount:
             reservation.discount_code = discount
            else:
                reservation.discount_code = None

            reservation.save()

              # Send an email notification
            subject = 'Reservation Confirmation'
            from_email = settings.DEFAULT_FROM_EMAIL  # Use the default sender email from settings
            recipient_list = [form.cleaned_data['guest_email']]  # Assuming 'guest_email' is the field in your form
            # Render the email content using the template
            context = {
                'check_in_date': form.cleaned_data['check_in_date'],
                'check_out_date': form.cleaned_data['check_out_date'],
                'guest_name':form.cleaned_data["guest_name"],
                'reservation_date':datetime.now(),
                'check_in_time': form.cleaned_data["check_in_time"],
                'check_out_time': form.cleaned_data["check_out_time"],
                # Add other context variables as needed
             }
            html_message = render_to_string('email.html', context)
            plain_message = strip_tags(html_message)  # Create a plain text message for non-HTML email clients

            email = EmailMultiAlternatives(subject, plain_message, from_email, recipient_list)
            email.attach_alternative(html_message, "text/html")  # Attach the HTML content

            email.send()

            return redirect("index")  # Redirect to a success page
        else:
            # Handle the case where there are not enough available rooms
            form.add_error(
                None,
                f"Not enough available rooms of type '{room_type}' for the selected dates.",
            )
            print("not valid")
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add check_in_date and check_out_date to the template context
        context["check_in_date"] = self.request.POST.get("check_in_date")
        context["check_out_date"] = self.request.POST.get("check_out_date")

        # Add any additional context data you need for the reservation form
        context["available_rooms"] = Room.objects.filter(
            id__in=RoomAvailability.objects.filter(
                date__range=[context["check_in_date"], context["check_out_date"]],
                is_available=True,
            ).values("room_id")
        )
 
        unavailable_dates = UnavailableDate.objects.values_list('date', flat=True)
        context['unavailable_dates'] = unavailable_dates
        print(unavailable_dates)
        return context


class ReservationSuccessView(View):
    template_name = "reservation_success.html"

    def get(self, request):
        # This is a placeholder view for displaying a success message or page after a reservation is made.
        return render(request, self.template_name)


def testReserve(request):
    return render(request, "sample3.html")


def validate_discount_code(request):
    discount_code = request.GET.get("discount_code")
    if discount_code:
        try:
            discount = Discount.objects.get(
                discountCode=discount_code, discountActive=True
            )
            return JsonResponse(
                {"valid": True, "discount_price": discount.discountPrice}
            )
        except Discount.DoesNotExist:
            pass
    return JsonResponse({"valid": False})
