import datetime
from Reservation.models import Facility, Reservations


def check_availability(facility, checkIn, checkOut):
    avail_list=[]
    reservationList = Reservations.objects.filter(facility=facility)
    for reservation in reservationList:
        if reservation.checkIn > checkOut or reservation.checkOut<checkOut:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)


def check_availability2(Prices, checkIn, checkOut, timeIn, timeOut):
    avail_list=[]
    reservationList = Reservations.objects.filter(checkIn=checkIn)
    print(reservationList)
    for reservation in reservationList:
        if reservation.checkIn > checkOut or reservation.checkOut<checkIn:
            if reservation.timeIn != timeIn:
                print(reservation.timeIn)
                print(timeIn)
                avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)