import datetime
from .models import Booking, Room, Hotel

def check_availibilty(room, check_in, check_out, capacity, pk):
    avail_list = []
    otel = Hotel.objects.get(pk=pk)
    booking_list = otel.booked_rooms.all()
    last_booking_list = booking_list.filter(room=room)
    capacity_list = otel.rooms.all()
    last_capacity_list = capacity_list.filter(name=room)
    for booking in last_booking_list:
        for capa_city in last_capacity_list:
            if (booking.check_in >= check_out or booking.check_out <= check_in) and capa_city.capacity >= capacity:
                avail_list.append(True)
            else:
                avail_list.append(False)
    return all(avail_list)