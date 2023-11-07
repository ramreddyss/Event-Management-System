# in your forms.py (create this file in the same directory as models.py if it doesn't exist)
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'  # this will include all fields from the Event model
