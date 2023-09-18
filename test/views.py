from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from .models import Reservation, Room, RoomAvailability
from .forms import ReservationForm
import random

# Create your views here.
class ReservationCreateView(FormView):
    template_name = 'sample3.html'
    form_class = ReservationForm
    print('in')
    def form_valid(self, form):
        print('valid form')
      # Retrieve form data
        check_in_date = form.cleaned_data['check_in_date']
        check_out_date = form.cleaned_data['check_out_date']
        room_type = form.cleaned_data['room_type']
        num_rooms = form.cleaned_data['num_rooms']

        # Find available rooms of the selected room type
        available_rooms = Room.objects.filter(room_type=room_type)

        # Filter available rooms by checking reservations
        reserved_rooms = Reservation.objects.filter(
            room__in=available_rooms,
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date,
        ).values_list('room', flat=True)

        # Exclude reserved rooms from available rooms
        available_rooms = available_rooms.exclude(id__in=reserved_rooms)

        if available_rooms.count() >= num_rooms:
            # Randomly select available rooms up to the requested number
            selected_rooms = random.sample(list(available_rooms), num_rooms)

            # Create a single reservation for the selected rooms
            reservation = Reservation.objects.create(
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                guest_name=form.cleaned_data['guest_name'],
                guest_email=form.cleaned_data['guest_email'],
                guest_phone=form.cleaned_data['guest_phone'],
                num_guests=form.cleaned_data['num_guests'],
            )
            reservation.room.set(selected_rooms)  # Set the selected rooms for the reservation

            return redirect('index')  # Redirect to a success page
        else:
            # Handle the case where there are not enough available rooms
            form.add_error(None, f"Not enough available rooms of type '{room_type}' for the selected dates.")
            print('not valid')
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add check_in_date and check_out_date to the template context
        context['check_in_date'] = self.request.POST.get('check_in_date')
        context['check_out_date'] = self.request.POST.get('check_out_date')

        # Add any additional context data you need for the reservation form
        context['available_rooms'] = Room.objects.filter(
            id__in=RoomAvailability.objects.filter(
                date__range=[context['check_in_date'], context['check_out_date']],
                is_available=True
            ).values('room_id')
        )
        return context
    


class ReservationSuccessView(View):
    template_name = 'reservation_success.html'

    def get(self, request):
        # This is a placeholder view for displaying a success message or page after a reservation is made.
        return render(request, self.template_name)


def testReserve(request):
    return render(request, 'sample3.html')