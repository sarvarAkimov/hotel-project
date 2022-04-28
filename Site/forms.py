
from django import forms
from .models import Grading, Hotel

class AddGrading(forms.ModelForm):
    class Meta:
        model = Grading
        fields = ('review_text', 'grade')


        
    
        