from django import forms
from myapp.models import LoginInfo4
from crispy_bootstrap5.bootstrap5 import Switch

    

class LoginInfo3(forms.ModelForm):
    class Meta:
        model = LoginInfo4
        fields = '__all__'
        
from django import forms
from .models import Place
from mapbox_location_field.forms import LocationField

class PlaceForm(forms.ModelForm):
    location = LocationField(map_attrs={"style": "mapbox://styles/mapbox/streets-v11"})

    class Meta:
        model = Place
        fields = ['name', 'location']
        
        
        
# forms.py

from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(label='Address', max_length=100)




# forms.py

from django import forms
from .models import CustomerFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = ['text']
