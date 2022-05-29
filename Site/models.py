
from tabnanny import check
from tkinter import N
from django.db import models

from accounts.models import People

# Create your models here.
# 1
# Hotel qo'shish
class Hotel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=150, verbose_name='ism')
    state = models.CharField(max_length=100, verbose_name='viloyat')
    city = models.CharField(max_length=100, verbose_name='tuman')
    street = models.CharField(max_length=200, verbose_name='manzil')
    image = models.ImageField(upload_to='images', verbose_name='rasm')
    agent_name = models.ForeignKey('Agent', on_delete=models.CASCADE, null=False, verbose_name='ishchi')
    types = models.ManyToManyField('Room_type', verbose_name='xonalar turi')
    comforts_list = models.ManyToManyField('Comforts', verbose_name='qulayliklar')
    rating = models.ManyToManyField('Rating', verbose_name='reyting')
    distance = models.ManyToManyField('Distance', verbose_name='markazdan masofa')
    grade = models.ManyToManyField('Grading', verbose_name='baho', blank=True)
    additional = models.ManyToManyField('Additional', verbose_name="Qo'shimcha hizmatlar")
    room_comforts = models.ManyToManyField('Room_comforts', verbose_name='Xonadagi qulayliklar')
    about = models.TextField(verbose_name='mehmonhona haqida')
    average = models.FloatField(verbose_name="o'rtacha baho")
    viewed = models.ManyToManyField(People, blank=True, verbose_name="ko'rilgan")
    viewed_count = models.IntegerField(blank=True, verbose_name="ko'rilgan soni")
    rooms = models.ManyToManyField('Room', verbose_name='honalar')
    booked_rooms = models.ManyToManyField('Booking', verbose_name='zakaz honalar', blank=True)


    def __str__(self):
        return f"{self.name}-{self.state}"

class Agent(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=150, verbose_name='ism')
    phone = models.BigIntegerField(verbose_name='telefon raqam')

    def __str__(self):
        return f"{self.name}"


class Room_type(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Comforts(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Rating(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Distance(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Additional(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Room_comforts(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


# 2
# Baholash otellarni
GRADE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Grading(models.Model):
    user = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='foydalanuvchi')
    ide = models.AutoField(primary_key=True, unique=True)
    review_text = models.TextField(verbose_name='sharh qoldirish')
    grade = models.IntegerField(choices=GRADE, null=True, blank=True, verbose_name='baho')

    def __str__(self):
        return f"{self.grade}"

# 3
# Hona ZAKAZ qilish
class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(verbose_name='hona nomi', max_length=150)
    capacity = models.IntegerField(verbose_name="hona sig'imi")

    def __str__(self):
        return f"{self.name}"


class Booking(models.Model):

    user = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='buyurtmachi')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='hona')
    check_in = models.DateField(verbose_name='...dan')
    check_out = models.DateField(verbose_name='...gacha')
    otel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Otel nomi')


    def __str__(self):
        return f"{self.user} booked room-{self.room} in {self.otel}"








