from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from django.views.generic.edit import FormView, UpdateView
from .models import Reservation, Room, UnavailableDate
from .forms import ReservationForm, ExtendedForm, ReservationEditForm
import random
from django.http import JsonResponse
from Reservation.models import Discount, Facility
from datetime import datetime
from decimal import Decimal
from captcha.fields import ReCaptchaField


# Create your views here.
class ReservationCreateView(FormView):
    template_name = "public.html"
    form_class = ReservationForm
    print("in")

    def form_valid(self, form):
        print("valid form")
        print(form.cleaned_data["captcha"])
        # Retrieve form data

        check_in_date = form.cleaned_data["check_in_date"]
        check_out_date = form.cleaned_data["check_out_date"]
        check_in_time = form.cleaned_data["check_in_time"]
        check_out_time = form.cleaned_data["check_out_time"]
        room_type = form.cleaned_data["room_type"]
        num_rooms = form.cleaned_data["num_rooms"]
        cottage_type = form.cleaned_data["cottage_type"]
        num_cottage = form.cleaned_data["num_cottage"]
        discount_code = form.cleaned_data[
            "discount_code"
        ]  # Get the discount_code value
        reservation_type = "public"
        num_guests = form.cleaned_data["num_guests"]
        reservation_time = form.cleaned_data["reservation_time"]

        total = getTotal(reservation_type, reservation_time, num_guests)
        decTotal = Decimal(total)

        print(decTotal)

        if discount_code:
            try:
                discount = Discount.objects.get(
                    discountCode=discount_code, discountActive=True
                )
                discPrice = discount.discountPrice
                total = decTotal - discPrice
            except Discount.DoesNotExist:
                # Handle the case where the discount code is not valid or not active
                discount = None
                return None
        else:
            discount = None  # No discount code provided, set discount to None

        available_rooms = Room.objects.filter(id=0)
        if room_type != None:
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
            print(room_type)
            print(int(num_rooms or 0))
        selected_rooms = []
        if room_type != None and available_rooms.count() >= num_rooms:
            # Randomly select available rooms up to the requested number
            selected_rooms = random.sample(list(available_rooms), num_rooms)
            print(selected_rooms)
            print(type(selected_rooms))
        else:
            # Handle the case where there are not enough available rooms
            if room_type != None:
                form.add_error(
                    None,
                    f"Not enough available rooms of type '{room_type}' for the selected dates.",
                )
                print("not valid")
                return self.form_invalid(form)

        available_cottage = Room.objects.filter(id=0)
        if cottage_type != None:
            # Find available rooms of the selected room type
            available_cottage = Room.objects.filter(room_type=cottage_type)

            # Filter available rooms by checking reservations
            reserved_cottage = Reservation.objects.filter(
                room__in=available_cottage,
                check_in_date__lte=check_out_date,
                check_out_date__gte=check_in_date,
            ).values_list("room", flat=True)

            # Exclude reserved rooms from available rooms
            available_rooms = available_rooms.exclude(id__in=reserved_cottage)
            print(cottage_type)
            print(int(num_cottage or 0))
            selected_cottages=None
        if cottage_type != None and available_cottage.count() >= num_cottage:
            # Randomly select available rooms up to the requested number
            selected_cottages = random.sample(list(available_cottage), num_cottage)
            
            selected_rooms.extend(selected_cottages)
            print(selected_cottages)
            print(selected_rooms)
        else:
            # Handle the case where there are not enough available rooms
            if cottage_type != None:
                form.add_error(
                    None,
                    f"Not enough available cottage of type '{cottage_type}' for the selected dates.",
                )
                print("not valid")
                return self.form_invalid(form)

            # Create a single reservation for the selected rooms
        reservation = Reservation.objects.create(
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guest_name=form.cleaned_data["guest_name"],
            guest_email=form.cleaned_data["guest_email"],
            guest_phone=form.cleaned_data["guest_phone"],
            num_guests=num_guests,
            reservation_time=form.cleaned_data["reservation_time"],
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            total=total,
            reservation_type=reservation_type,
        )
        if room_type != None or cottage_type !=None:
            # Set the selected rooms for the reservation
            reservation.room.set(selected_rooms)
            for room in selected_rooms:
                total = decTotal + room.price_per_night
                print("total: ", total)
                price = Facility.objects.get(
                    facilityName=reservation_type + " " + reservation_time
                )
                print(room.free_guests)
                print(num_guests)
                print("check:", room.free_guests < num_guests)
                if room.free_guests > num_guests:
                    print("true")
                    free = num_guests * price.facilityPrice
                else:
                    free = room.free_guests * price.facilityPrice
                print("free: ", free)
                decTotal = total - free
                print("Total: ", decTotal)
                reservation.total = decTotal

        # You can add more calculations here based on your business logic

        # Associate the discount code with the reservation
        if discount:
            reservation.discount_code = discount
        else:
            reservation.discount_code = None

        room_details = []
        reservation.save()
        if room_type != None or cottage_type!= None:
            room_details = []
            for room in selected_rooms:
                room_details.append(
                    {
                        "room_number": room.room_number,
                        "room_type": room.room_type.facilityName,
                        "price": room.price_per_night,
                    }
                )

        reference_number = reservation.reference_number
        #   # Send an email notification
        strSubject = "Reservation Confirmation " + str(reference_number)
        subject = strSubject
        from_email = (
            settings.DEFAULT_FROM_EMAIL
        )  # Use the default sender email from settings
        recipient_list = [
            form.cleaned_data["guest_email"]
        ]  # Assuming 'guest_email' is the field in your form
        # Render the email content using the template
        context = {
            "reserve": {
                "referenceNum": reservation.reference_number,
                "customer": reservation.guest_name,
                "checkIn": reservation.check_in_date,
                "timeIn": reservation.check_in_time,
                "checkOut": reservation.check_out_date,
                "timeOut": reservation.check_out_time,
                "date": reservation.date,
                "status": reservation.status,
                #'prices': reservation.room.price,
                "discount": discount,
                #'downpayment': reservation.downpayment,
                #'balance': reservation.balance,
                "total": reservation.total,
                "num_guest": reservation.num_guests,
                #'totalPax':
                "room": room_details,
                "type": reservation_type,
                "time": reservation_time,
                "total_pax": decTotal,
            }
        }
        html_message = render_to_string("reference.html", context)
        plain_message = strip_tags(
               html_message
        )  # Create a plain text message for non-HTML email clients

        email = EmailMultiAlternatives(
            subject, plain_message, from_email, recipient_list
        )
        email.attach_alternative(
            html_message, "text/html"
        )  # Attach the HTML content

        # email.send()

        # Construct the URL for the summary page, passing the reference number as a parameter
        summary_url = reverse("reservation_summary", args=[reference_number])
        return redirect(summary_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add check_in_date and check_out_date to the template context
        context["check_in_date"] = self.request.POST.get("check_in_date")
        context["check_out_date"] = self.request.POST.get("check_out_date")

        context["active_facilities"] = Facility.objects.filter(facilityActive=True)

        unavailable_dates = UnavailableDate.objects.values_list("date", flat=True)
        context["unavailable_dates"] = unavailable_dates
        print(unavailable_dates)
        print(context["active_facilities"])
        return context


class ReservationCreateViewPrivate(FormView):
    template_name = "private.html"
    form_class = ExtendedForm
    print("in")

    def form_valid(self, form):
        print("valid form")
        print(form.cleaned_data["captcha"])
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
        reservation_type = "private"
        num_guests = form.cleaned_data["num_guests_select"]
        reservation_time = form.cleaned_data["reservation_time"]
        cottage_type = form.cleaned_data["cottage_type"]
        num_cottage = form.cleaned_data["num_cottage"]

        total = getTotal(reservation_type, reservation_time, num_guests)
        decTotal = Decimal(total)

        print(decTotal)

        if discount_code:
            try:
                discount = Discount.objects.get(
                    discountCode=discount_code, discountActive=True
                )
                discPrice = discount.discountPrice
                total = decTotal - discPrice
            except Discount.DoesNotExist:
                # Handle the case where the discount code is not valid or not active
                discount = None
                return None
        else:
            discount = None  # No discount code provided, set discount to None

        available_rooms = Room.objects.filter(id=0)
        if room_type != None:
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
            print(room_type)
            print(int(num_rooms or 0))
        selected_rooms = []
        if room_type != None and available_rooms.count() >= num_rooms:
            # Randomly select available rooms up to the requested number
            selected_rooms = random.sample(list(available_rooms), num_rooms)
            print(selected_rooms)
            print(type(selected_rooms))
        else:
            # Handle the case where there are not enough available rooms
            if room_type != None:
                form.add_error(
                    None,
                    f"Not enough available rooms of type '{room_type}' for the selected dates.",
                )
                print("not valid")
                return self.form_invalid(form)

        available_cottage = Room.objects.filter(id=0)
        if cottage_type != None:
            # Find available rooms of the selected room type
            available_cottage = Room.objects.filter(room_type=cottage_type)

            # Filter available rooms by checking reservations
            reserved_cottage = Reservation.objects.filter(
                room__in=available_cottage,
                check_in_date__lte=check_out_date,
                check_out_date__gte=check_in_date,
            ).values_list("room", flat=True)

            # Exclude reserved rooms from available rooms
            available_rooms = available_rooms.exclude(id__in=reserved_cottage)
            print(cottage_type)
            print(int(num_cottage or 0))
            selected_cottages=None
        if cottage_type != None and available_cottage.count() >= num_cottage:
            # Randomly select available rooms up to the requested number
            selected_cottages = random.sample(list(available_cottage), num_cottage)
            
            selected_rooms.extend(selected_cottages)
            print(selected_cottages)
            print(selected_rooms)
        else:
            # Handle the case where there are not enough available rooms
            if cottage_type != None:
                form.add_error(
                    None,
                    f"Not enough available cottage of type '{cottage_type}' for the selected dates.",
                )
                print("not valid")
                return self.form_invalid(form)
        


        reservation = Reservation.objects.create(
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guest_name=form.cleaned_data["guest_name"],
            guest_email=form.cleaned_data["guest_email"],
            guest_phone=form.cleaned_data["guest_phone"],
            num_guests=num_guests,
            reservation_time=form.cleaned_data["reservation_time"],
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            total=total,
            reservation_type=reservation_type,
        )
        if room_type != None or cottage_type !=None:
            # Set the selected rooms for the reservation
            reservation.room.set(selected_rooms)
            for room in selected_rooms:
                total = Decimal(total) + room.price_per_night
                decTotal = total
                print("Total: ", decTotal)
                reservation.total = decTotal
        # You can add more calculations here based on your business logic

        # Associate the discount code with the reservation
        if discount:
            reservation.discount_code = discount
        else:
            reservation.discount_code = None

        room_details = []
        reservation.save()
        if reservation_type == "private":
                UnavailableDate.objects.create(
                    date=check_in_date,
                )
        if room_type != None or cottage_type!= None:
            room_details = []
            for room in selected_rooms:
                room_details.append(
                    {
                        "room_number": room.room_number,
                        "room_type": room.room_type.facilityName,
                        "price": room.price_per_night,
                    }
                )

        reference_number = reservation.reference_number
        #   # Send an email notification
        strSubject = "Reservation Confirmation " + str(reference_number)
        subject = strSubject
        from_email = (
            settings.DEFAULT_FROM_EMAIL
        )  # Use the default sender email from settings
        recipient_list = [
            form.cleaned_data["guest_email"]
        ]  # Assuming 'guest_email' is the field in your form
        # Render the email content using the template
        context = {
            "reserve": {
                "referenceNum": reservation.reference_number,
                "customer": reservation.guest_name,
                "checkIn": reservation.check_in_date,
                "timeIn": reservation.check_in_time,
                "checkOut": reservation.check_out_date,
                "timeOut": reservation.check_out_time,
                "date": reservation.date,
                "status": reservation.status,
                #'prices': reservation.room.price,
                "discount": discount,
                #'downpayment': reservation.downpayment,
                #'balance': reservation.balance,
                "total": reservation.total,
                "num_guest": reservation.num_guests,
                #'totalPax':
                "room": room_details,
                "type": reservation_type,
                "time": reservation_time,
                "total_pax": decTotal,
            }
        }
        html_message = render_to_string("reference.html", context)
        plain_message = strip_tags(
               html_message
        )  # Create a plain text message for non-HTML email clients

        email = EmailMultiAlternatives(
            subject, plain_message, from_email, recipient_list
        )
        email.attach_alternative(
            html_message, "text/html"
        )  # Attach the HTML content

        # email.send()

        # Construct the URL for the summary page, passing the reference number as a parameter
        summary_url = reverse("reservation_summary", args=[reference_number])
        return redirect(summary_url)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add check_in_date and check_out_date to the template context
        context["check_in_date"] = self.request.POST.get("check_in_date")
        context["check_out_date"] = self.request.POST.get("check_out_date")

        context["active_facilities"] = Facility.objects.filter(facilityActive=True)

        unavailable_dates = UnavailableDate.objects.values_list("date", flat=True)
        context["unavailable_dates"] = unavailable_dates
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


class ReservationSummaryView(View):
    template_name = "reference.html"

    def get(self, request, reference_number):
        reservation = get_object_or_404(Reservation, reference_number=reference_number)

        # Add any other logic you need to prepare data for the summary page
        reservation_type = reservation.reservation_type
        reservation_time = reservation.reservation_time
        num_guests = reservation.num_guests
        print(reservation_time)
        print(reservation_type)
        total_pax = getTotal(reservation_type, reservation_time, num_guests)
        rooms = reservation.room.all()
        print(total_pax)
        # Create a list to store room details
        room_details = []
        price = 0
        if reservation_type == "private":
            price = Facility.objects.get(
                facilityName=reservation_type + " " + reservation_time,
                facilitymax=num_guests,
            )
        elif reservation_type == "public":
            price = Facility.objects.get(
                facilityName=reservation_type + " " + reservation_time
            )
        # Loop through associated rooms and get price and type
        for room in rooms:
            room_details.append(
                {
                    "room_number": room.room_number,
                    "room_type": room.room_type.facilityName,
                    "price": room.price_per_night,
                    "free": computeFreeGuest(num_guests, room.free_guests),
                    "free_price": computeFree(num_guests, room.free_guests, price),
                }
            )

        discount = 0
        if reservation.discount_code != None:
            discount = reservation.discount_code.discountPrice
        else:
            discount = 0
        context = {
            "reserve": {
                "referenceNum": reservation.reference_number,
                "customer": reservation.guest_name,
                "checkIn": reservation.check_in_date,
                "timeIn": reservation.check_in_time,
                "checkOut": reservation.check_out_date,
                "timeOut": reservation.check_out_time,
                "date": reservation.date,
                "status": reservation.status,
                #'prices': reservation.room.price,
                "discount": discount,
                #'downpayment': reservation.downpayment,
                #'balance': reservation.balance,
                "total": reservation.total,
                "num_guest": reservation.num_guests,
                #'totalPax':
                "room": room_details,
                "type": reservation_type,
                "time": reservation_time,
                "total_pax": total_pax,
            }
        }
        return render(request, self.template_name, context)


def computeFreeGuest(num_guests, free_guests):
    if num_guests < free_guests:
        free = num_guests
    else:
        free = free_guests
    return free


def computeFree(num_guests, free_guests, price):
    if num_guests < free_guests:
        free = num_guests * price.facilityPrice
    else:
        free = free_guests * price.facilityPrice
    return free


def getTotal(reservation_type, reservation_time, num_guests):
    total = 0.00
    price = []
    if reservation_type == "public":
        num_guests = num_guests
        price = Facility.objects.get(
            facilityName=reservation_type + " " + reservation_time
        )
        total = price.facilityPrice * num_guests
        print(total)
    elif reservation_type == "private":
        # num_guests = num_guests_select
        print(type)
        price = Facility.objects.get(
            facilityName=reservation_type + " " + reservation_time,
            facilitymax=int(num_guests),
        )
        total = price.facilityPrice
        print(total)

    return total


class ReservationUpdateView(UpdateView):
    model = Reservation
    template_name = "edit.html"  # Use the same template as in your create view
    form_class = ReservationEditForm
    success_url = "/staff"

    def form_valid(self, form):
        print("valid form")
        print(form.cleaned_data["captcha"])
        # Retrieve form data

        check_in_date = form.cleaned_data["check_in_date"]
        check_out_date = form.cleaned_data["check_out_date"]
        check_in_time = form.cleaned_data["check_in_time"]
        check_out_time = form.cleaned_data["check_out_time"]
        room_type = form.cleaned_data["room"]
        num_rooms = form.cleaned_data["num_rooms"]
        discount_code = form.cleaned_data[
            "discount_code"
        ]  # Get the discount_code value
        reservation_type = "public"
        num_guests = form.cleaned_data["num_guests"]
        reservation_time = form.cleaned_data["reservation_time"]

        total = getTotal(reservation_type, reservation_time, num_guests)
        decTotal = Decimal(total)

        print(decTotal)

        if discount_code:
            try:
                discount = Discount.objects.get(
                    discountCode=discount_code, discountActive=True
                )
                discPrice = discount.discountPrice
                total = decTotal - discPrice
            except Discount.DoesNotExist:
                # Handle the case where the discount code is not valid or not active
                discount = None
                return None
        else:
            discount = None  # No discount code provided, set discount to None

        available_rooms = Room.objects.filter(id=0)
        if room_type != None:
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

        if available_rooms.count() >= num_rooms or room_type == None:
            # Randomly select available rooms up to the requested number
            selected_rooms = random.sample(list(available_rooms), num_rooms)

            # Create a single reservation for the selected rooms
            reservation = Reservation.objects.create(
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                guest_name=form.cleaned_data["guest_name"],
                guest_email=form.cleaned_data["guest_email"],
                guest_phone=form.cleaned_data["guest_phone"],
                num_guests=num_guests,
                reservation_time=form.cleaned_data["reservation_time"],
                check_in_time=check_in_time,
                check_out_time=check_out_time,
                total=total,
                reservation_type=reservation_type,
                room=room_type,
            )
            if room_type != None:
                # Set the selected rooms for the reservation
                reservation.room.set(selected_rooms)
                for room in selected_rooms:
                    total = Decimal(total) + room.price_per_night
                    print("total: ", total)
                    price = Facility.objects.get(
                        facilityName=reservation_type + " " + reservation_time
                    )
                    print(room.free_guests)
                    print(num_guests)
                    print("check:", room.free_guests < num_guests)
                    if room.free_guests > num_guests:
                        print("true")
                        free = num_guests * price.facilityPrice
                    else:
                        free = room.free_guests * price.facilityPrice
                    print("free: ", free)
                    decTotal = total - free
                    print("Total: ", decTotal)
                    reservation.total = decTotal

            # You can add more calculations here based on your business logic

            # Associate the discount code with the reservation
            if discount:
                reservation.discount_code = discount
            else:
                reservation.discount_code = None

            room_details = []
            reservation.save()
            if room_type != None:
                room_details = []
                for room in selected_rooms:
                    room_details.append(
                        {
                            "room_number": room.room_number,
                            "room_type": room.room_type.facilityName,
                            "price": room.price_per_night,
                        }
                    )

            reference_number = reservation.reference_number
            #   # Send an email notification
            strSubject = "Reservation Confirmation " + str(reference_number)
            subject = strSubject
            from_email = (
                settings.DEFAULT_FROM_EMAIL
            )  # Use the default sender email from settings
            recipient_list = [
                form.cleaned_data["guest_email"]
            ]  # Assuming 'guest_email' is the field in your form
            # Render the email content using the template
            context = {
                "reserve": {
                    "referenceNum": reservation.reference_number,
                    "customer": reservation.guest_name,
                    "checkIn": reservation.check_in_date,
                    "timeIn": reservation.check_in_time,
                    "checkOut": reservation.check_out_date,
                    "timeOut": reservation.check_out_time,
                    "date": reservation.date,
                    "status": reservation.status,
                    #'prices': reservation.room.price,
                    "discount": discount,
                    #'downpayment': reservation.downpayment,
                    #'balance': reservation.balance,
                    "total": reservation.total,
                    "num_guest": reservation.num_guests,
                    #'totalPax':
                    "room": room_details,
                    "type": reservation_type,
                    "time": reservation_time,
                    "total_pax": decTotal,
                    "status": form.cleaned_data["status"],
                }
            }
            html_message = render_to_string("reference.html", context)
            plain_message = strip_tags(
                html_message
            )  # Create a plain text message for non-HTML email clients

            email = EmailMultiAlternatives(
                subject, plain_message, from_email, recipient_list
            )
            email.attach_alternative(
                html_message, "text/html"
            )  # Attach the HTML content

            email.send()

            # Construct the URL for the summary page, passing the reference number as a parameter
            summary_url = reverse("reservation_summary", args=[reference_number])
            return redirect(summary_url)

            return redirect("index")
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

        # Add any additional context data you need for rendering the form
        # ...

        # You may need to modify the following lines based on your context requirements
        # context["check_in_date"] = self.object.check_in_date
        # context["check_out_date"] = self.object.check_out_date
        context["active_facilities"] = Facility.objects.filter(facilityActive=True)
        unavailable_dates = UnavailableDate.objects.values_list("date", flat=True)
        context["unavailable_dates"] = unavailable_dates

        return context
