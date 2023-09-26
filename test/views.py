from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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
from Reservation.models import Discount, Facility
from datetime import datetime
from decimal import Decimal
from captcha.fields import ReCaptchaField


pip


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
        total_pax=getTotal(reservation_type, reservation_time, num_guests, num_guests)
        rooms=reservation.room.all()
        print(total_pax)
        # Create a list to store room details
        room_details = []

        # Loop through associated rooms and get price and type
        for room in rooms:
            room_details.append({
                'room_number': room.room_number,
                'room_type': room.room_type.room_type,
                'price': room.price_per_night,
            })
        discount = 0
        if reservation.discount_code != None:
            discount = reservation.discount_code.discountPrice
        else:
            discount = 0
        context = {
            'reserve': {
                'referenceNum': reservation.reference_number,
                'customer': reservation.guest_name,
                'checkIn': reservation.check_in_date,
                'timeIn': reservation.check_in_time,
                'checkOut': reservation.check_out_date,
                'timeOut': reservation.check_out_time,
                'date': reservation.date,
                'status': reservation.status,
                #'prices': reservation.room.price,
                'discount': discount,
                #'downpayment': reservation.downpayment,
                #'balance': reservation.balance,
                'total': reservation.total,
                'num_guest' : reservation.num_guests,
                #'totalPax':
                'room' : room_details, 
                'type' : reservation_type,
                'time' :reservation_time,
                'total_pax':total_pax,
            }
        }

        return render(request, self.template_name, context)
    

def getTotal(reservation_type, reservation_time, num_guests, num_guests_select):
    total=0.00
    price = []
    print(num_guests_select)
    if reservation_type == 'public':
        num_guests = num_guests
        price = Facility.objects.get(facilityName = reservation_type+' '+reservation_time)
        total =  price.facilityPrice
        print (total)
    elif reservation_type == 'private':
        num_guests = num_guests_select
        print(type)
        price = Facility.objects.get(facilityName = reservation_type+' ' +reservation_time, facilitymax = int(num_guests))
        total =  price.facilityPrice
        print(total)

    return total