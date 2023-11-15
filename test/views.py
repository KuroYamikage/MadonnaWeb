from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView, UpdateView
from .models import Reservation, Room, UnavailableDate, Prices, Payment
from .forms import (
    ReservationForm,
    ExtendedForm,
    ReservationEditForm,
    PriceForm,
    PublicExtendedForm,
)
import random
import json

from datetime import date, timedelta
import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from Reservation.models import Discount, Facility
from datetime import datetime, timedelta
from decimal import Decimal
from captcha.fields import ReCaptchaField
from django.contrib.auth.mixins import LoginRequiredMixin
from workalendar.asia import Philippines

from django.contrib import messages





# Create your views here.
class ReservationCreateView(FormView):
    template_name = "public.html"
    form_class = PublicExtendedForm
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
        num_child = form.cleaned_data["num_child"]

        reservation_type = "public"
        num_guests = form.cleaned_data["num_guests"]
        reservation_time = form.cleaned_data["reservation_time"]
        event_hall = form.cleaned_data['event_hall']
        print('Event Hall',type(event_hall))


        total = getTotal(
            reservation_type,
            reservation_time,
            num_guests,
            num_child,
            check_in_date,
            False,
        )
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
            available_cottage = available_cottage.exclude(id__in=reserved_cottage)
            print(cottage_type)
            print(int(num_cottage or 0))
            selected_cottages = None
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
        print(event_hall == 'False')
        if event_hall == 'True':
            print('here')
            available_cottage = Room.objects.filter(id=0)
            if event_hall == 'True':
                # Find available rooms of the selected room type
                available_cottage = Room.objects.filter(room_type=7)

                # Filter available rooms by checking reservations
                reserved_cottage = Reservation.objects.filter(
                    room__in=available_cottage,
                    check_in_date__lte=check_out_date,
                    check_out_date__gte=check_in_date,
                ).values_list("room", flat=True)

                # Exclude reserved rooms from available rooms
                available_cottage = available_cottage.exclude(id__in=reserved_cottage)
                print(available_cottage, "eh")
                selected_cottages = None
                print(available_cottage.count(), "eh")
            if event_hall == 'True' and available_cottage.count() >= 1:
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
                        f"Event Hall not Available for the selected dates.",
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
            num_child=num_child,
            pool =  form.cleaned_data['pool'],
        )
        if room_type != None or cottage_type != None:
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
        if room_type != None or cottage_type != None:
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
        email.attach_alternative(html_message, "text/html")  # Attach the HTML content

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

        unavailable_dates = UnavailableDate.objects.all
        context["unavailable_dates"] = unavailable_dates
        print(context["active_facilities"])
        return context


class ReservationCreateViewPrivate(FormView):
    template_name = "private.html"
    form_class = ExtendedForm
    print("in")
    def form_invalid(self, form):
        # Print form errors to console
        print(form.errors)
        return super().form_invalid(form)
    def form_valid(self, form):
        print("valid form")
        print(form.cleaned_data["captcha"])
        # Retrieve form data

        check_in_date = form.cleaned_data["check_in_date"]
        check_out_date = form.cleaned_data["check_out_date"]
        check_in_time = form.cleaned_data["check_in_time"]
        check_out_time = form.cleaned_data["check_out_time"]
        # # room_type = form.cleaned_data["room_type"]
        # # num_rooms = form.cleaned_data["num_rooms"]
        discount_code = form.cleaned_data[
            "discount_code"
        ]  # Get the discount_code value
        reservation_type = "private"
        num_guests = form.cleaned_data["num_guests_select"]
        reservation_time = form.cleaned_data["reservation_time"]
        # cottage_type = form.cleaned_data["cottage_type"]
        # num_cottage = form.cleaned_data["num_cottage"]
        withRoom = form.cleaned_data["withRoom"]
        event_hall = form.cleaned_data["event_hall"]
        print("With Room? ",withRoom)
        total = getTotal(
            reservation_type, reservation_time, num_guests, 0, check_in_date, withRoom
        )
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
        selected_rooms=[]
        print(event_hall)
        if event_hall == 'True':
            print('here')
            available_cottage = Room.objects.filter(id=0)
            if event_hall == 'True':
                # Find available rooms of the selected room type
                available_cottage = Room.objects.filter(room_type=7)

                # Filter available rooms by checking reservations
                reserved_cottage = Reservation.objects.filter(
                    room__in=available_cottage,
                    check_in_date__lte=check_out_date,
                    check_out_date__gte=check_in_date,
                ).values_list("room", flat=True)

                # Exclude reserved rooms from available rooms
                available_cottage = available_cottage.exclude(id__in=reserved_cottage)
                print(available_cottage, "eh")
                selected_cottages = None
                print(available_cottage.count(), "eh")
            if event_hall == 'True' and available_cottage.count() >= 1:
                # Randomly select available rooms up to the requested number
                selected_cottages = random.sample(list(available_cottage),1)

                selected_rooms = random.sample(list(available_cottage), 1)
                print(selected_cottages)
                print(selected_rooms)
            else:
                # Handle the case where there are not enough available rooms
                if event_hall == 'True':
                    form.add_error(
                        None,
                        f"Event Hall not Available for the selected dates.",
                    )
                    print("not valid")
                    return self.form_invalid(form)
        # if room_type != None:
        #     # Find available rooms of the selected room type
        #     available_rooms = Room.objects.filter(room_type=room_type)

        #     # Filter available rooms by checking reservations
        #     reserved_rooms = Reservation.objects.filter(
        #         room__in=available_rooms,
        #         check_in_date__lte=check_out_date,
        #         check_out_date__gte=check_in_date,
        #     ).values_list("room", flat=True)

        #     # Exclude reserved rooms from available rooms
        #     available_rooms = available_rooms.exclude(id__in=reserved_rooms)
        #     print(room_type)
        #     print(int(num_rooms or 0))
        # selected_rooms = []
        # if room_type != None and available_rooms.count() >= num_rooms:
        #     # Randomly select available rooms up to the requested number
        #     selected_rooms = random.sample(list(available_rooms), num_rooms)
        #     print(selected_rooms)
        #     print(type(selected_rooms))
        # else:
        #     # Handle the case where there are not enough available rooms
        #     if room_type != None:
        #         form.add_error(
        #             None,
        #             f"Not enough available rooms of type '{room_type}' for the selected dates.",
        #         )
        #         print("not valid")
        #         return self.form_invalid(form)

        # available_cottage = Room.objects.filter(id=0)
        # if cottage_type != None:
        #     # Find available rooms of the selected room type
        #     available_cottage = Room.objects.filter(room_type=cottage_type)

        #     # Filter available rooms by checking reservations
        #     reserved_cottage = Reservation.objects.filter(
        #         room__in=available_cottage,
        #         check_in_date__lte=check_out_date,
        #         check_out_date__gte=check_in_date,
        #     ).values_list("room", flat=True)

        #     # Exclude reserved rooms from available rooms
        #     available_rooms = available_rooms.exclude(id__in=reserved_cottage)
        #     print(cottage_type)
        #     print(int(num_cottage or 0))
        #     selected_cottages = None
        # if cottage_type != None and available_cottage.count() >= num_cottage:
        #     # Randomly select available rooms up to the requested number
        #     selected_cottages = random.sample(list(available_cottage), num_cottage)

        #     selected_rooms.extend(selected_cottages)
        #     print(selected_cottages)
        #     print(selected_rooms)
        # else:
        #     # Handle the case where there are not enough available rooms
        #     if cottage_type != None:
        #         form.add_error(
        #             None,
        #             f"Not enough available cottage of type '{cottage_type}' for the selected dates.",
        #         )
        #         print("not valid")
        #         return self.form_invalid(form)

        reservation = Reservation.objects.create(
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guest_name=form.cleaned_data["guest_name"],
            guest_email=form.cleaned_data["guest_email"],
            guest_phone=form.cleaned_data["guest_phone"],
            num_guests=num_guests,
            reservation_time=form.cleaned_data["reservation_time"],
            pool=form.cleaned_data["pool"],
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            total=total,
            reservation_type=reservation_type,
            withRoom = withRoom,
        )
        if event_hall == 'True':
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
            if UnavailableDate.objects.filter(dates = check_in_date).exists():
                obj = get_object_or_404(UnavailableDate, dates=check_in_date)

                # Step 2: Modify the object's attribute (column)
                if form.cleaned_data['pool'] == 'Pool 1':
                    obj.pool1 = True

                elif form.cleaned_data['pool'] == 'Pool 2':
                    obj.pool2 = True
                # Step 3: Save changes to the database
                obj.save()
            else:
                if form.cleaned_data['pool'] == 'Pool 1':
                    UnavailableDate.objects.create(
                        dates=check_in_date,
                        pool1 = True,
                    )

                elif form.cleaned_data['pool'] == 'Pool 2':
                    UnavailableDate.objects.create(
                        dates=check_in_date,
                        pool2 = True,
                    )
                    
        if event_hall == 'True':
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
        email.attach_alternative(html_message, "text/html")  # Attach the HTML content

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

        unavailable_dates = UnavailableDate.objects.all
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
        check_in_date = reservation.check_in_date
        num_child = reservation.num_child
        withRoom = reservation.withRoom
        print(reservation_time)
        print(reservation_type)
        total_pax = getTotal(
            reservation_type,
            reservation_time,
            num_guests,
            num_child,
            check_in_date,
            withRoom,
        )
        rooms = reservation.room.all()
        print(rooms)
        # Create a list to store room details
        room_details = []
        price = 0
        if reservation_type == "private":
            reservation_type1 ="Private"
            price = Prices.objects.get(
                type=reservation_type1,
                time = reservation_time,
                maxPax=num_guests,
                withRoom = withRoom
            )
        elif reservation_type == "public":
            price = Facility.objects.get(
                facilityName=reservation_type + " " + reservation_time
            )
        # Loop through associated rooms and get price and type
        downpayment = 0
        for room in rooms:
            if reservation_type == 'public':
                downpayment = downpayment + room.price_per_night
                room_details.append(
                {
                    "room_number": room.room_number,
                    "room_type": room.room_type.facilityName,
                    "price": room.price_per_night,
                    "free": computeFreeGuest(num_guests, room.free_guests),
                    "free_price": computeFree(num_guests, room.free_guests, price),
                }
                )
            elif reservation_type == 'private':
                room_details.append(
                {
                    "room_number": room.room_number,
                    "room_type": room.room_type.facilityName,
                    "price": room.price_per_night,
                }
                )

        if reservation_type == 'private':
            downpayment=reservation.total / 2
        discount = 0
        print("downpayment:", downpayment)
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
                "pool": reservation.pool,
                "num_child":reservation.num_child,
                "withRoom" : reservation.withRoom,
                "payments":reservation.payments,
                "downpayment":downpayment
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


def getTotal(
    reservation_type, reservation_time, num_guests, num_child, check_in_date, withRoom
):
    total = 0.00
    price = []
    date_object = datetime.strptime(str(check_in_date), "%Y-%m-%d")

    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week = date_object.weekday()

    # Map the numeric representation to the day name
    day_name = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ][day_of_week]

    day_classifier = ""

    if (
        day_name == "Monday"
        or day_name == "Tuesday"
        or day_name == "Wednesday"
        or day_name == "Thursday"
    ):
        day_classifier = "Weekday"
    else:
        day_classifier = "Weekend"

    cal = Philippines()

    # Check if the date is a holiday
    is_holiday = cal.is_working_day(date_object)

    # Print the result
    if is_holiday:
        day_classifier = "Weekend"

    # Print the result
    if reservation_time == "Morning":
            reservation_time = "Day"

    if reservation_type == "public":
        reservation_type = "Public"
        num_guests = num_guests
        priceAdult = Prices.objects.get(
            type=reservation_type,
            time=reservation_time,
            guest="Adult",
            date=day_classifier,
        )
        print(priceAdult.price)
        priceChild = Prices.objects.get(
            type=reservation_type,
            time=reservation_time,
            guest="Child",
            date=day_classifier,
        )
        print(priceChild.price)
        totalAdult = priceAdult.price * num_child
        print(totalAdult)
        totalChild = priceChild.price * num_guests
        print(totalChild)
        total = totalChild + totalAdult
        print(total)
    elif reservation_type == "private":
        reservation_type = "Private"
        # num_guests = num_guests_select
        print(reservation_type)
        print(reservation_time)
        print(int(num_guests))
        print(withRoom)
        price = Prices.objects.get(
            type=reservation_type,
            time=reservation_time,
            maxPax=int(num_guests),
            withRoom=withRoom,
        )
        total = price.price
        print(total)

    return total


class ReservationUpdateView(UpdateView):
    # model = Reservation
    # template_name = "edit.html"  # Use the same template as in your create view
    # form_class = ReservationEditForm
    # success_url = "/staff"

    # def form_valid(self, form):
    #     print("valid form")
    #     print(form.cleaned_data["captcha"])
    #     # Retrieve form data

    #     check_in_date = form.cleaned_data["check_in_date"]
    #     check_out_date = form.cleaned_data["check_out_date"]
    #     check_in_time = form.cleaned_data["check_in_time"]
    #     check_out_time = form.cleaned_data["check_out_time"]
    #     room_type = form.cleaned_data["room"]
    #     num_rooms = form.cleaned_data["num_rooms"]
    #     discount_code = form.cleaned_data[
    #         "discount_code"
    #     ]  # Get the discount_code value
    #     reservation_type = form.cleaned_data['reservation_type']
    #     num_guests = form.cleaned_data["num_guests"]
    #     reservation_time = form.cleaned_data["reservation_time"]
    #     num_child = form.cleaned_data["num_child"]
    #     withRoom = False

    #     if reservation_type== 'public':
    #         num_child = form.cleaned_data["num_child"]
    #         num_guests = form.cleaned_data["num_guests"]
    #         withRoom = False
    #     elif reservation_type =='private':
    #         num_child = 0
    #         num_guests = form.cleaned_data["num_guests_select"]
    #         withRoom = form.cleaned_data["withRoom"]

    #     total = getTotal(
    #         reservation_type,
    #         reservation_time,
    #         num_guests,
    #         num_child,
    #         check_in_date,
    #         withRoom,
    #     )
    #     decTotal = Decimal(total)
    #     selected_rooms = []
    #     print(decTotal)

    #     if discount_code:
    #         try:
    #             discount = Discount.objects.get(
    #                 discountCode=discount_code, discountActive=True
    #             )
    #             discPrice = discount.discountPrice
    #             total = decTotal - discPrice
    #         except Discount.DoesNotExist:
    #             # Handle the case where the discount code is not valid or not active
    #             discount = None
    #             return None
    #     else:
    #         discount = None  # No discount code provided, set discount to None

    #     available_rooms = Room.objects.filter(id=0)
    #     if room_type != None:
    #         # Find available rooms of the selected room type
    #         available_rooms = Room.objects.filter(room_type=room_type)

    #         # Filter available rooms by checking reservations
    #         reserved_rooms = Reservation.objects.filter(
    #             room__in=available_rooms,
    #             check_in_date__lte=check_out_date,
    #             check_out_date__gte=check_in_date,
    #         ).values_list("room", flat=True)

    #         # Exclude reserved rooms from available rooms
    #         available_rooms = available_rooms.exclude(id__in=reserved_rooms)

    #     if available_rooms.count() >= num_rooms or room_type == None:
    #         # Randomly select available rooms up to the requested number
    #         selected_rooms = random.sample(list(available_rooms), num_rooms)

            
    #     # Create a single reservation for the selected rooms
    #     reservation = Reservation.objects.create(
    #     check_in_date=check_in_date,
    #     check_out_date=check_out_date,
    #     guest_name=form.cleaned_data["guest_name"],
    #     guest_email=form.cleaned_data["guest_email"],
    #     guest_phone=form.cleaned_data["guest_phone"],
    #     num_guests=num_guests,
    #     reservation_time=form.cleaned_data["reservation_time"],
    #     check_in_time=check_in_time,
    #     check_out_time=check_out_time,
    #     total=total,
    #     reservation_type=reservation_type,
    #     room=room_type,
    #     num_child = num_child,
    #     withRoom = withRoom,
    #     )
    #     if room_type != None:
    #         # Set the selected rooms for the reservation
    #         reservation.room.set(selected_rooms)
    #         for room in selected_rooms:
    #             total = Decimal(total) + room.price_per_night
    #             print("total: ", total)
    #             price = Facility.objects.get(
    #                 facilityName=reservation_type + " " + reservation_time
    #             )
    #             print(room.free_guests)
    #             print(num_guests)
    #             print("check:", room.free_guests < num_guests)
    #             if room.free_guests > num_guests:
    #                 print("true")
    #                 free = num_guests * price.facilityPrice
    #             else:
    #                 free = room.free_guests * price.facilityPrice
    #             print("free: ", free)
    #             decTotal = total - free
    #             print("Total: ", decTotal)
    #             reservation.total = decTotal

    #         # You can add more calculations here based on your business logic

    #         # Associate the discount code with the reservation
    #         if discount:
    #             reservation.discount_code = discount
    #         else:
    #             reservation.discount_code = None

    #         room_details = []
    #         reservation.save()
    #         if room_type != None:
    #             room_details = []
    #             for room in selected_rooms:
    #                 room_details.append(
    #                     {
    #                         "room_number": room.room_number,
    #                         "room_type": room.room_type.facilityName,
    #                         "price": room.price_per_night,
    #                     }
    #                 )

    #         reference_number = reservation.reference_number
    #         #   # Send an email notification
    #         strSubject = "Reservation Confirmation " + str(reference_number)
    #         subject = strSubject
    #         from_email = (
    #             settings.DEFAULT_FROM_EMAIL
    #         )  # Use the default sender email from settings
    #         recipient_list = [
    #             form.cleaned_data["guest_email"]
    #         ]  # Assuming 'guest_email' is the field in your form
    #         # Render the email content using the template
    #         context = {
    #             "reserve": {
    #                 "referenceNum": reservation.reference_number,
    #                 "customer": reservation.guest_name,
    #                 "checkIn": reservation.check_in_date,
    #                 "timeIn": reservation.check_in_time,
    #                 "checkOut": reservation.check_out_date,
    #                 "timeOut": reservation.check_out_time,
    #                 "date": reservation.date,
    #                 "status": reservation.status,
    #                 #'prices': reservation.room.price,
    #                 "discount": discount,
    #                 #'downpayment': reservation.downpayment,
    #                 #'balance': reservation.balance,
    #                 "total": reservation.total,
    #                 "num_guest": reservation.num_guests,
    #                 #'totalPax':
    #                 "room": room_details,
    #                 "type": reservation_type,
    #                 "time": reservation_time,
    #                 "total_pax": decTotal,
    #                 "status": form.cleaned_data["status"],
    #             }
    #         }
    #         html_message = render_to_string("reference.html", context)
    #         plain_message = strip_tags(
    #             html_message
    #         )  # Create a plain text message for non-HTML email clients

    #         email = EmailMultiAlternatives(
    #             subject, plain_message, from_email, recipient_list
    #         )
    #         email.attach_alternative(
    #             html_message, "text/html"
    #         )  # Attach the HTML content

    #         email.send()

    #         # Construct the URL for the summary page, passing the reference number as a parameter
    #         summary_url = reverse("reservation_summary", args=[reference_number])
    #         return redirect(summary_url)

    #     else:
    #         # Handle the case where there are not enough available rooms
    #         form.add_error(
    #             None,
    #             f"Not enough available rooms of type '{room_type}' for the selected dates.",
    #         )
    #         print("not valid")
    #         return self.form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # Add any additional context data you need for rendering the form
    #     # ...

    #     # You may need to modify the following lines based on your context requirements
    #     # context["check_in_date"] = self.object.check_in_date
    #     # context["check_out_date"] = self.object.check_out_date
    #     context["active_facilities"] = Facility.objects.filter(facilityActive=True)
       
    #     unavailable_dates = UnavailableDate.objects.all
    #     context["unavailable_dates"] = unavailable_dates

    #     return context
    model = Reservation
    template_name = "edit.html"  # Replace with your actual template name
    form_class = ReservationEditForm

    def form_valid(self, form):
        
        messages.success(self.request, 'Reservation updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating reservation.')
        return super().form_invalid(form)

    def get_success_url(self):
        success_url = "/staff"
        return reverse(success_url)  # Replace with your actual success URL name


# class AvailableRoomsView(View):
#     def get(self, request, *args, **kwargs):
#         selected_date = request.GET.get('selected_date')
#         # Perform logic to get available room choices for the selected date
#         available = UnavailableDate.objects.filter( dates = selected_date)
#         if available.exists():
#         available_rooms = available
#         return JsonResponse({'available_rooms': available_rooms})


class priceCreate(LoginRequiredMixin, CreateView):
    form_class = PriceForm
    template_name = "newPrice.html"
    success_url = "../price/"


class priceList(LoginRequiredMixin, ListView):
    model = Prices
    context_object_name = "price"
    template_name = "priceList.html"


class priceUpdate(LoginRequiredMixin, UpdateView):
    model = Prices
    form_class = PriceForm
    success_message = "List succcesfully edited"
    success_url = "../price/"
    template_name = "editPrice.html"
    login_url = "login"

def process_payment(request):
    if request.method == 'POST':
        # Get the tokenized card information from the frontend (Paymongo.js)
        token = request.POST.get('paymongoToken')

        # Make a request to Paymongo to create a payment
        secret_key = settings.PAYMONGO_SECRET_KEY
        print(secret_key)
        headers = {
            'Authorization': f'Basic {secret_key}',
            'Content-Type': 'application/json',
        }
        data = {
            'data': {
                'attributes': {
                    'amount': 10000,  # Replace with your amount in cents
                    'payment_method_allowed': ['card'],
                    'payment_method_options': {
                        'card': {
                            'request_three_d_secure': 'automatic',
                        },
                    },
                },
                'relationships': {
                    'payment_method': {
                        'data': {
                            'id': token,
                            'type': 'payment_method',
                        },
                    },
                },
            },
        }

        response = requests.post('https://api.paymongo.com/v2/payments', headers=headers, json=data)

        if response.status_code == 200:
            # Payment successful, update your payment model or perform other actions
            Payment.objects.create(amount=10000, status='success', payment_method_id=token)
            return JsonResponse({'success': True, 'message': 'Payment successful'})
        else:
            # Payment failed, handle accordingly
            Payment.objects.create(amount=10000, status='failed', payment_method_id=token)
            return JsonResponse({'success': False, 'message': 'Payment failed'})
    return render(request, 'payments/payment_form.html', {'public_key':settings.PAYMONGO_PUBLIC_KEY})






def room_availability(request):
    # Get all rooms
    rooms = Room.objects.all()

    # Get reservations for the current day
    reservations_today = Reservation.objects.filter(
        check_in_date__lte=timezone.now().date(),
        check_out_date__gte=timezone.now().date()
    )

    # Create a dictionary to store room availability status
    room_availability_status = {}

    # Populate the dictionary with room availability status
    for room in rooms:
        is_available = not reservations_today.filter(room=room).exists()
        room_availability_status[room] = is_available

    return render(request, 'availability.html', {'room_availability_status': room_availability_status})

def room_availability_weekly(request):
    # Retrieve all rooms
    rooms = Room.objects.all()

    # Define the start and end dates of the week
    today = date.today()
    start_date = today - timedelta(days=today.weekday())  # Monday of the current week
    end_date = start_date + timedelta(days=6)  # Sunday of the current week

    # Generate a list of dates for the week
    week_days = [start_date + timedelta(days=i) for i in range(7)]

    # Create a list to store room availability status
    room_availability_status = []

    for day in week_days:
        availability_dict = {'day': day, 'availability': {}}

        # Check the availability status for each room
        for room in rooms:
            # Assume availability checking logic here
            is_available = check_room_availability(room, day)
            availability_dict['availability'][room] = is_available

            # Debug prints

        room_availability_status.append(availability_dict)

    print(f"Room Availability Status: {room_availability_status}")
    context = {
        'room_availability_status': room_availability_status,
        'rooms': rooms,
        'week_days': week_days,
    }

    return render(request, 'room_availability_weekly.html', context)

def check_room_availability(room, date):
    # Get reservations for the specified room on the given date
    reservations = Reservation.objects.filter(room=room, check_in_date__lte=date, check_out_date__gt=date)

    # Check if any of the reservations have the room associated
    for reservation in reservations:
        if room in reservation.room.all():
            return False  # Room is reserved for this date

    return True  # Room is available for this date


def payment_success(request):
    reference = request.GET.get('reference', 'DefaultStringValue')
    reservation = get_object_or_404(Reservation, reference_number=reference)
    downpayment = request.GET.get('downpayment', 'DefaultStringValue')
    reservation.payments = downpayment
    reservation.status = 'Approved'
    print(reservation.status)
    print(reservation.payments)
    reservation.save()
    print(reference)
    return render(request, 'payments/payment_success.html', {'refNum': reference})

def payment_failure(request):
    reference_number = request.GET.get('reference')
    if reference_number:
        # Redirect to reservation_summary view with the reference number
        return redirect(reverse('reservation_summary', args=[reference_number]))
    else:
        # Handle the case where there's no reference number in the query string
        return HttpResponse("Payment failed without a reference number.")


def pay_test(request):
    url = "https://api.paymongo.com/v1/checkout_sessions"
    param1_value = request.GET.get('param1', 'default_value1')
    print("Raw param1_value:", param1_value)
    param2_value = request.GET.get('param2', 'default_value2')
    rooms=[]
    failure_url = request.build_absolute_uri(reverse('payment_failure')) + f'?reference={param1_value}'
    reservation = get_object_or_404(Reservation, reference_number=param1_value)
    rooms = reservation.room.all()
    room_details = []
    print(rooms)
    num_guests = reservation.num_guests
    reservation_type = reservation.reservation_type
    reservation_time = reservation.reservation_time
    withRoom = reservation.withRoom
    total=0
    price=0
    if reservation_type == "private":
            reservation_type1 ="Private"
            price = Prices.objects.get(
                type=reservation_type1,
                time = reservation_time,
                maxPax=num_guests,
                withRoom = withRoom
            )
    elif reservation_type == "public":
            price = Facility.objects.get(
                facilityName=reservation_type + " " + reservation_time
            )
    for room in rooms:
            room_details.append(
                {
                    "room_number": room.room_number,
                    "room_type": room.room_type.facilityName,
                    "price": room.price_per_night,
                }
            )
    line_items = []

    included = []
    if reservation_type == "public":
        for x in room_details: 
            print("this is x ",x)
            total = total+x['price']
            line_items.append({
                "currency": "PHP",
                "amount": int(x['price']*100),
                "description": x["room_number"],
                "quantity": 1,
                "name": x['room_type'] # Assuming 'room_type' is a key in your dictionary
            })
    elif reservation_type == 'private':
        
        total = reservation.total/2
        line_items.append({
                "currency": "PHP",
                "amount": int(total*100),
                "description": 'Half of the Reservation Total',
                "quantity": 1,
                "name": 'Downpayment' # Assuming 'room_type' is a key in your dictionary
            })
        

    print(line_items)

    print("Line Items", line_items)
    payload = {
        "data": {
            "attributes": {
                "send_email_receipt": False,
                "show_description": True,
                "show_line_items": True,
                "line_items": line_items,
                "description": "Reservation",
                "payment_method_types": ["gcash"],
                "success_url": request.build_absolute_uri(reverse('payment_success')) + f'?reference={param1_value}&downpayment={total}',
                "failure_url": failure_url,
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic c2tfdGVzdF90dFdrQmtjem9EZ1g2ZEoyVDVmSm5kVm06MTIzNDU="  # Replace with your actual base64-encoded public key
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()

        
        

        if response.status_code == 200:
            # Redirect the user to the Paymongo HTML checkout page
            checkout_url = data.get('data', {}).get('attributes', {}).get("checkout_url")
            response = HttpResponseRedirect(checkout_url)
            return response
        else:
            return JsonResponse({"error": "Failed to retrieve checkout URL"}, status=500)

    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)


 
    

