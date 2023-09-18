from django import forms
from .models import Room, Reservation, RoomAvailability, RoomType

class ReservationForm(forms.ModelForm):
    room_type = forms.ModelChoiceField(
        queryset=RoomType.objects.all(),
        required=True,
        empty_label=None,  # To force users to select a room type
    )
    
    num_rooms = forms.IntegerField(
        required=True,
        min_value=1,  # Require at least 1 room
    )
    class Meta:
        model = Reservation
        fields = [
            'room',
            'check_in_date',
            'check_out_date',
            'guest_name',
            'guest_email',
            'guest_phone',
            'num_guests',
            'room_type',
            'num_rooms',
        ]

    # Add a room_type field to your form

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)

        # You can customize the form fields here if needed

        # Example: Limit room choices to available rooms
        self.fields['room'].queryset = Room.objects.filter(
            id__in=RoomAvailability.objects.filter(is_available=True).values('room_id')
        )
        super().__init__(*args, **kwargs)
        # Set the 'required' attribute of the 'room' field to False
        self.fields['room'].required = False