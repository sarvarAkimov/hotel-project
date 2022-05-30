
from django import forms
from .models import Grading, Hotel, Booking, Room


class AddGrading(forms.ModelForm):
    class Meta:
        model = Grading
        fields = ('review_text', 'grade')

all_rooms = Room.objects.all()
ROOMS = []
for room in all_rooms:
    ROOMS.append([room.name, room.name])

class AvailibiltyForm(forms.Form):
    capacity = forms.IntegerField(required=True)
    check_in = forms.DateField(required=True, widget=forms.SelectDateWidget)
    check_out = forms.DateField(required=True, widget=forms.SelectDateWidget)

class BookRoom(forms.Form):
    room = forms.ChoiceField(choices=ROOMS, required=True)



        
    
        