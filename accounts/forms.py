from django.contrib.auth.forms import UserCreationForm
from .models import People

class PersonCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = People
        fields = ('username', 'first_name', 'last_name', 'email')