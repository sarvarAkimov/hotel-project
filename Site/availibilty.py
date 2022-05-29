import datetime
from .models import Booking, Room, Hotel

def check_availibilty(room, check_in, check_out, pk):
    avail_list = []
    otel = Hotel.objects.get(pk=pk)
    booking_list = otel.booked_rooms.all()
    last_booking_list = booking_list.filter(room=room)
    # booking_list = Booking.objects.filter(room=room)
    for booking in last_booking_list:
        if booking.check_in >= check_out or booking.check_out < check_in or booking.check_in > check_out or booking.check_out <= check_in or (booking.check_in > check_out or booking.check_out < check_in):
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)