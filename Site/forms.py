
from ast import Try
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
    room = forms.ChoiceField(choices=ROOMS, required=True)
    check_in = forms.DateField(input_formats=["%d-%m-%Y"], required=True, widget=forms.DateField)
    check_out = forms.DateField(input_formats=["%d-%m-%Y"], required=True)


        
    
        