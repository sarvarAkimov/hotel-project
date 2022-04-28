import django_filters
from django import forms

from django.db import models
from .models import Hotel, Room_type, Comforts, Rating, Distance, Additional, Room_comforts
from django.forms.widgets import TextInput


class HotelFilter(django_filters.FilterSet):
    CHOICES1 = [
        ['Toshkent', 'Toshkent'],
        ['Namangan', 'Namangan'],
        ['Andijon', 'Andijon'],
    ]

    all_room_type = Room_type.objects.all()
    ROOMTYPES = []
    for room_type in all_room_type:
        ROOMTYPES.append([room_type.id, room_type.name])

    all_comforts = Comforts.objects.all()
    COMFORTS = []
    for comfort in all_comforts:
        COMFORTS.append([comfort.id, comfort.name])

    all_ratings = Rating.objects.all()
    RATINGS = []
    for rating in all_ratings:
        RATINGS.append([rating.id, rating.name])
    
    all_distances = Distance.objects.all()
    DISTANCES = []
    for distance in all_distances:
        DISTANCES.append([distance.id, distance.name])

    all_additionals = Additional.objects.all()
    ADDITIONALS = []
    for addition in all_additionals:
        ADDITIONALS.append([addition.id, addition.name])

    all_room_comforts = Room_comforts.objects.all()
    ROOMCOMFORTS = []
    for room_comfort in all_room_comforts:
        ROOMCOMFORTS.append([room_comfort.id, room_comfort.name])

    # all_grades = Grade.objects.all()
    GRADES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
    # for grade in all_grades:
    #     GRADES.append([grade.id, grade.name])

    state = django_filters.MultipleChoiceFilter(label='Viloyat...', widget=forms.CheckboxSelectMultiple(), choices=CHOICES1)
    comforts_list = django_filters.MultipleChoiceFilter(choices=COMFORTS, widget=forms.CheckboxSelectMultiple(), conjoined=True)
    types = django_filters.MultipleChoiceFilter(choices=ROOMTYPES, widget=forms.CheckboxSelectMultiple(), conjoined=True)
    rating = django_filters.MultipleChoiceFilter(choices=RATINGS, widget=forms.CheckboxSelectMultiple(), conjoined=True)
    distance = django_filters.MultipleChoiceFilter(choices=DISTANCES, widget=forms.CheckboxSelectMultiple(), conjoined=True)
    additional = django_filters.MultipleChoiceFilter(choices=ADDITIONALS, widget=forms.CheckboxSelectMultiple(), conjoined=True)
    room_comforts = django_filters.MultipleChoiceFilter(choices=ROOMCOMFORTS, widget=forms.CheckboxSelectMultiple(), conjoined=True)
    grade = django_filters.MultipleChoiceFilter(choices=GRADES, widget=forms.CheckboxSelectMultiple(), conjoined=True)

    class Meta:
        model = Hotel
        fields = ['name']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'label': 'Имя отеля'
                },
            }
        }
