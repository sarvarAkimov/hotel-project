from django.contrib import admin
from .models import Hotel, Agent, Room_type, Comforts, Rating, Room_comforts, Distance, Additional, Grading
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Agent)
admin.site.register(Room_type)
admin.site.register(Comforts)
admin.site.register(Rating)
admin.site.register(Room_comforts)
# admin.site.register(Grade)
admin.site.register(Distance)
admin.site.register(Additional)
admin.site.register(Grading)