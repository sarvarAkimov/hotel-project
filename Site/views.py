from winreg import CreateKey
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Hotel, Grading
from .filters import HotelFilter
from .forms import AddGrading
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
    comments = post.grade.all
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
    return render(request, 'Site/card_page.html', {'post': post, 'form':form, 'comments': comments})



def count(request, pk):
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




