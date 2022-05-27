from tabnanny import check
from winreg import CreateKey
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from Site.availibilty import check_availibilty
from accounts.models import People
from .models import Hotel, Grading, Room, Booking
from .filters import HotelFilter
from .forms import AddGrading, AvailibiltyForm
from django.views.generic.edit import CreateView

# Create your views here.


class MainPage(ListView):
    model = Hotel
    template_name = 'Site/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = HotelFilter(self.request.GET, queryset=self.get_queryset())     
        return context


def hotel_details(request, pk):
    user = request.user
    form = AddGrading()
    post = Hotel.objects.get(pk=pk)
    post.viewed.add(user)
    post.viewed_count = post.viewed.count()
    post.save()
    if request.method == "POST":
        form = AddGrading(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            hotel = Hotel.objects.get(pk=pk)
            post.otel = hotel
            post.save()
            hotel.grade.add(post)
            return redirect('hotel-detail', pk=pk)
    return render(request, 'Site/card_page.html', {'post': post, 'form':form})



def count(request,pk):
    hotel = Hotel.objects.get(id=pk)
    all_hotels_grade = hotel.grade.all()
    average_stars  = 0
    for one_hotels_grade in all_hotels_grade:
        average_stars += int(one_hotels_grade.grade)
    try: 

        average_score = round(average_stars/len(all_hotels_grade), 1)*2
        hotel.average = average_score
        hotel.save()
        return HttpResponse(f'{average_score}')
        
    except ZeroDivisionError:
        return HttpResponse('0')

def booking_view(request):
    form = AvailibiltyForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        room_list = Room.objects.filter(name=data['room'])
        avail_rooms = []
        for room in room_list:
            if check_availibilty(room, check_in=data['check_in'], check_out=data['check_out']):
                avail_rooms.append(room)
        
        if len(avail_rooms) > 0:
            roomss = avail_rooms[0]
            booking = Booking.objects.create(
                user = request.user,
                room = roomss,
                check_in = data['check_in'],
                check_out = data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('this room is booked')

    return render(request, 'Site/booking_form.html', {'form':form})



